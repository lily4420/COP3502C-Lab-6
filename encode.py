{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPEKs73nH+s7g0FeMe+6BWH",
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
        "<a href=\"https://colab.research.google.com/github/lily4420/COP3502C-Lab-6/blob/main/encode.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "76MSJI4-RUla"
      },
      "outputs": [],
      "source": [
        "# lily kurek's encode and main function\n",
        "\n",
        "def menu():\n",
        "  print('\\nMenu')\n",
        "  print('-------------')\n",
        "  print('1. Encode')\n",
        "  print('2. Decode')\n",
        "  print('3. Quit')\n",
        "\n",
        "def main():\n",
        "  end_program = False\n",
        "  while end_program == False:\n",
        "    print(menu())\n",
        "    user_input = int(input('Please enter an option: '))\n",
        "    if user_input == 1:\n",
        "      user_password = input('Please enter your password to encode: ')\n",
        "      encode(user_password)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "def encode(password):\n",
        "  encoded_password = ''\n",
        "  for i in password:\n",
        "    i = int(i) + 3\n",
        "    encoded_password += str(i)\n",
        "  return encoded_password\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "main()"
      ]
    }
  ]
}