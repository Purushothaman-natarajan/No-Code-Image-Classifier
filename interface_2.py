{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45708f1b-77a3-4fbb-bc5a-8b57a1950a64",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\purus\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\tqdm\\auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Keyboard interruption in main thread... closing server.\n"
     ]
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "import subprocess\n",
    "\n",
    "# Define wrapper functions for each script\n",
    "def run_data_loader(path, target_folder, dim, batch_size, num_workers, augment_data):\n",
    "    command = [\n",
    "        \"python\", \"data_loader.py\",\n",
    "        \"--path\", path,\n",
    "        \"--target_folder\", target_folder,\n",
    "        \"--dim\", str(dim),\n",
    "        \"--batch_size\", str(batch_size),\n",
    "        \"--num_workers\", str(num_workers)\n",
    "    ]\n",
    "    if augment_data:\n",
    "        command.append(\"--augment_data\")\n",
    "    \n",
    "    result = subprocess.run(command, capture_output=True, text=True)\n",
    "    return result.stdout if result.returncode == 0 else f\"Error: {result.stderr}\"\n",
    "\n",
    "def run_train(base_models, shape, data_path, log_dir, model_dir, epochs, optimizer, learning_rate, batch_size):\n",
    "    command = [\n",
    "        \"python\", \"train.py\",\n",
    "        \"--base_models\", ','.join(base_models),\n",
    "        \"--shape\", shape,\n",
    "        \"--data_path\", data_path,\n",
    "        \"--log_dir\", log_dir,\n",
    "        \"--model_dir\", model_dir,\n",
    "        \"--epochs\", str(epochs),\n",
    "        \"--optimizer\", optimizer,\n",
    "        \"--learning_rate\", str(learning_rate),\n",
    "        \"--batch_size\", str(batch_size)\n",
    "    ]\n",
    "    \n",
    "    result = subprocess.run(command, capture_output=True, text=True)\n",
    "    return result.stdout if result.returncode == 0 else f\"Error: {result.stderr}\"\n",
    "\n",
    "def run_test(model_dir, img_path, log_dir, test_dir, train_dir, class_names):\n",
    "    command = [\n",
    "        \"python\", \"test.py\",\n",
    "        \"--model_dir\", model_dir,\n",
    "        \"--log_dir\", log_dir\n",
    "    ]\n",
    "    if img_path:\n",
    "        command.extend([\"--img_path\", img_path])\n",
    "    if test_dir:\n",
    "        command.extend([\"--test_dir\", test_dir])\n",
    "    if train_dir:\n",
    "        command.extend([\"--train_dir\", train_dir])\n",
    "    if class_names:\n",
    "        command.extend([\"--class_names\"] + class_names.split(\",\"))\n",
    "    \n",
    "    result = subprocess.run(command, capture_output=True, text=True)\n",
    "    return result.stdout if result.returncode == 0 else f\"Error: {result.stderr}\"\n",
    "\n",
    "def run_predict(model_path, img_path, train_dir):\n",
    "    command = [\n",
    "        \"python\", \"predict.py\",\n",
    "        \"--model_path\", model_path,\n",
    "        \"--img_path\", img_path,\n",
    "        \"--train_dir\", train_dir\n",
    "    ]\n",
    "    \n",
    "    result = subprocess.run(command, capture_output=True, text=True)\n",
    "    return result.stdout if result.returncode == 0 else f\"Error: {result.stderr}\"\n",
    "\n",
    "# Create Gradio interfaces\n",
    "data_loader_interface = gr.Interface(\n",
    "    fn=run_data_loader,\n",
    "    inputs=[\n",
    "        gr.Textbox(label=\"Path (Path to file)\"),\n",
    "        gr.Textbox(label=\"Target Folder (Path to directory)\"),\n",
    "        gr.Slider(minimum=1, maximum=512, value=224, label=\"Dimension\"),\n",
    "        gr.Slider(minimum=1, maximum=128, value=32, label=\"Batch Size\"),\n",
    "        gr.Slider(minimum=1, maximum=16, value=4, label=\"Number of Workers\"),\n",
    "        gr.Checkbox(label=\"Augment Data\")\n",
    "    ],\n",
    "    outputs=\"text\",\n",
    "    title=\"Data Loader\"\n",
    ")\n",
    "\n",
    "train_interface = gr.Interface(\n",
    "    fn=run_train,\n",
    "    inputs=[\n",
    "        gr.CheckboxGroup([\"VGG16\", \"VGG19\", \"ResNet50\", \"ResNet101\", \"InceptionV3\", \"DenseNet121\", \"MobileNetV2\", \"Xception\", \"InceptionResNetV2\", \"EfficientNetB0\"], label=\"Base Models\"),\n",
    "        gr.Textbox(value=\"224 224 3\", label=\"Shape\"),\n",
    "        gr.Textbox(label=\"Data Path (Path to file)\"),\n",
    "        gr.Textbox(label=\"Log Directory (Path to directory)\"),\n",
    "        gr.Textbox(label=\"Model Directory (Path to directory)\"),\n",
    "        gr.Slider(minimum=1, maximum=1000, value=100, label=\"Epochs\"),\n",
    "        gr.Dropdown([\"adam\", \"sgd\"], label=\"Optimizer\"),\n",
    "        gr.Number(value=0.0001, label=\"Learning Rate\"),\n",
    "        gr.Slider(minimum=1, maximum=128, value=32, label=\"Batch Size\")\n",
    "    ],\n",
    "    outputs=\"text\",\n",
    "    title=\"Training\"\n",
    ")\n",
    "\n",
    "test_interface = gr.Interface(\n",
    "    fn=run_test,\n",
    "    inputs=[\n",
    "        gr.File(label=\"Model Directory (Choose directory)\", type=\"directory\"),\n",
    "        gr.Image(type=\"filepath\", label=\"Image Path (optional, choose image)\"),\n",
    "        gr.Textbox(label=\"Log Directory (Path to directory)\"),\n",
    "        gr.Textbox(label=\"Test Directory (optional, Path to directory)\"),\n",
    "        gr.Textbox(label=\"Train Directory (optional, Path to directory)\"),\n",
    "        gr.Textbox(label=\"Class Names (optional, comma separated)\")\n",
    "    ],\n",
    "    outputs=\"text\",\n",
    "    title=\"Testing\"\n",
    ")\n",
    "\n",
    "predict_interface = gr.Interface(\n",
    "    fn=run_predict,\n",
    "    inputs=[\n",
    "        gr.File(label=\"Model Path (Choose file)\", type=\"file\"),\n",
    "        gr.Image(type=\"filepath\", label=\"Image Path (choose image)\"),\n",
    "        gr.Textbox(label=\"Train Directory (Path to directory)\")\n",
    "    ],\n",
    "    outputs=\"text\",\n",
    "    title=\"Prediction\"\n",
    ")\n",
    "\n",
    "gr.TabbedInterface([data_loader_interface, train_interface, test_interface, predict_interface], [\"Data Loader\", \"Training\", \"Testing\", \"Prediction\"]).launch(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": 3
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
