{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5b19a1e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Tag an image - remote =====\n"
     ]
    },
    {
     "ename": "ComputerVisionErrorResponseException",
     "evalue": "(InvalidRequest) Input data is not a valid image.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mComputerVisionErrorResponseException\u001b[0m      Traceback (most recent call last)",
      "Input \u001b[1;32mIn [6]\u001b[0m, in \u001b[0;36m<cell line: 44>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     42\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m===== Tag an image - remote =====\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     43\u001b[0m \u001b[38;5;66;03m# Call API with remote image\u001b[39;00m\n\u001b[1;32m---> 44\u001b[0m tags_result_remote \u001b[38;5;241m=\u001b[39m \u001b[43mcomputervision_client\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtag_image\u001b[49m\u001b[43m(\u001b[49m\u001b[43mremote_image_url\u001b[49m\u001b[43m \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     46\u001b[0m \u001b[38;5;66;03m# Print results with confidence score\u001b[39;00m\n\u001b[0;32m     47\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTags in the remote image: \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\azure\\cognitiveservices\\vision\\computervision\\operations\\_computer_vision_client_operations.py:593\u001b[0m, in \u001b[0;36mComputerVisionClientOperationsMixin.tag_image\u001b[1;34m(self, url, language, model_version, custom_headers, raw, **operation_config)\u001b[0m\n\u001b[0;32m    590\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_client\u001b[38;5;241m.\u001b[39msend(request, stream\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39moperation_config)\n\u001b[0;32m    592\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mstatus_code \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m [\u001b[38;5;241m200\u001b[39m]:\n\u001b[1;32m--> 593\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m models\u001b[38;5;241m.\u001b[39mComputerVisionErrorResponseException(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_deserialize, response)\n\u001b[0;32m    595\u001b[0m deserialized \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m    596\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mstatus_code \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m200\u001b[39m:\n",
      "\u001b[1;31mComputerVisionErrorResponseException\u001b[0m: (InvalidRequest) Input data is not a valid image."
     ]
    }
   ],
   "source": [
    "from azure.cognitiveservices.vision.computervision import ComputerVisionClient\n",
    "from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes\n",
    "from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes\n",
    "from msrest.authentication import CognitiveServicesCredentials\n",
    "\n",
    "from array import array\n",
    "import os\n",
    "from PIL import Image\n",
    "import sys\n",
    "import time\n",
    "\n",
    "'''\n",
    "Authenticate\n",
    "Authenticates your credentials and creates a client.\n",
    "'''\n",
    "subscription_key = \"4db7249d4a2f49059eb17a7d530bc5dd\"\n",
    "endpoint = \"https://aiblcomputervision.cognitiveservices.azure.com/\"\n",
    "\n",
    "computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))\n",
    "'''\n",
    "END - Authenticate\n",
    "'''\n",
    "\n",
    "'''\n",
    "Quickstart variables\n",
    "These variables are shared by several examples\n",
    "'''\n",
    "# Images used for the examples: Describe an image, Categorize an image, Tag an image, \n",
    "# Detect faces, Detect adult or racy content, Detect the color scheme, \n",
    "# Detect domain-specific content, Detect image types, Detect objects\n",
    "images_folder = os.path.join (os.path.dirname(os.path.abspath(\"C:\\\\Users\\\\skarasala\\\\Desktop\\\\Vineela\\\\Hackathon\")), \"images\")\n",
    "remote_image_url = \"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg\"\n",
    "'''\n",
    "END - Quickstart variables\n",
    "'''\n",
    "\n",
    "\n",
    "'''\n",
    "Tag an Image - remote\n",
    "This example returns a tag (key word) for each thing in the image.\n",
    "'''\n",
    "print(\"===== Tag an image - remote =====\")\n",
    "# Call API with remote image\n",
    "tags_result_remote = computervision_client.tag_image(remote_image_url )\n",
    "\n",
    "# Print results with confidence score\n",
    "print(\"Tags in the remote image: \")\n",
    "if (len(tags_result_remote.tags) == 0):\n",
    "    print(\"No tags detected.\")\n",
    "else:\n",
    "    for tag in tags_result_remote.tags:\n",
    "        print(\"'{}' with confidence {:.2f}%\".format(tag.name, tag.confidence * 100))\n",
    "print()\n",
    "'''\n",
    "END - Tag an Image - remote\n",
    "'''\n",
    "print(\"End of Computer Vision quickstart.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e359136",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
