{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "12Fr3fowkbbM6W58ofjWxrr2uyYBSi4qS",
      "authorship_tag": "ABX9TyOfO5Y1gtyerbsSQJaIoG3B",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/courtney-k/final458/blob/main/458webapp4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "\n",
        "# Load the model\n",
        "with open('random_forest_model3.pkl', 'rb') as model_file:\n",
        "    model = pickle.load(model_file)"
      ],
      "metadata": {
        "id": "KDYwUSK1FI3u"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pickle\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from sklearn.ensemble import RandomForestRegressor  # Import the RandomForestRegressor\n",
        "\n",
        "# Load the model\n",
        "with open('random_forest_model2.pkl', 'rb') as model_file:\n",
        "    model = pickle.load(model_file)\n",
        "\n",
        "# Check the type of the loaded object\n",
        "print(type(model))  # Print the type of the loaded object\n",
        "\n",
        "def main():\n",
        "    st.title(\"Salary Prediction App\")\n",
        "\n",
        "    # Collect user input\n",
        "    q11 = st.slider(\"Q11\", 0, 100, 50)\n",
        "    q30 = st.slider(\"Q30\", 0, 100, 50)\n",
        "    q27 = st.slider(\"Q27\", 0, 100, 50)\n",
        "    q26 = st.slider(\"Q26\", 0, 100, 50)\n",
        "    q23 = st.slider(\"Q23\", 0, 100, 50)\n",
        "\n",
        "    # Create a DataFrame with user input\n",
        "    input_data = pd.DataFrame({\n",
        "        'Q11': [q11],\n",
        "        'Q30': [q30],\n",
        "        'Q27': [q27],\n",
        "        'Q26': [q26],\n",
        "        'Q23': [q23]\n",
        "    })\n",
        "\n",
        "    # Make predictions\n",
        "    if isinstance(model, RandomForestRegressor):  # Check if the loaded object is a RandomForestRegressor\n",
        "        prediction = model.predict(input_data)\n",
        "        st.subheader(\"Prediction:\")\n",
        "        st.write(f\"The predicted salary is: {prediction[0]:.2f}\")\n",
        "    else:\n",
        "        st.write(\"Error: The loaded model is not a RandomForestRegressor.\")\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2q2Zns1pFdzB",
        "outputId": "ce8a0afe-c819-447a-a72b-2ecbf8632d28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'numpy.ndarray'>\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-12-11 13:59:15.164 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ]
    }
  ]
}