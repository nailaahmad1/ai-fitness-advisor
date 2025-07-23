{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fad686c5-263d-45c9-9b13-a4d2ada63904",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'openai'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 4\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# ai_fitness_advisor.py\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m----> 4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mopenai\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m# --- Set your OpenAI API key here ---\u001b[39;00m\n\u001b[0;32m      7\u001b[0m openai\u001b[38;5;241m.\u001b[39mapi_key \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myour-openai-api-key\u001b[39m\u001b[38;5;124m\"\u001b[39m  \u001b[38;5;66;03m# Replace with your real API key\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'openai'"
     ]
    }
   ],
   "source": [
    "# ai_fitness_advisor.py\n",
    "\n",
    "import streamlit as st\n",
    "import openai\n",
    "\n",
    "# --- Set your OpenAI API key here ---\n",
    "openai.api_key = \"your-openai-api-key\"  # Replace with your real API key\n",
    "\n",
    "st.set_page_config(page_title=\"AI Fitness Advisor\", page_icon=\"🏋️\")\n",
    "\n",
    "# --- App Header ---\n",
    "st.title(\"🏋️ FitMate: Your AI Fitness Advisor\")\n",
    "st.write(\"Get personalized workout and diet advice using AI!\")\n",
    "\n",
    "# --- User Input ---\n",
    "user_input = st.text_input(\"Tell me your fitness goal:\", placeholder=\"e.g., I want to lose weight in 4 weeks.\")\n",
    "\n",
    "# --- AI Prompt Template ---\n",
    "def generate_response(user_query):\n",
    "    prompt = f\"\"\"\n",
    "    You are a certified personal fitness coach. Based on the following user request, give a personalized fitness plan including exercises, schedule, and diet tips.\n",
    "    \n",
    "    User's request: {user_query}\n",
    "    \n",
    "    Provide a weekly workout plan (e.g., Mon to Sun), include what type of diet they should follow, and end with one motivational quote.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        response = openai.ChatCompletion.create(\n",
    "            model=\"gpt-3.5-turbo\",  # or \"gpt-4\" if available\n",
    "            messages=[\n",
    "                {\"role\": \"system\", \"content\": \"You are a helpful AI fitness coach.\"},\n",
    "                {\"role\": \"user\", \"content\": prompt}\n",
    "            ],\n",
    "            temperature=0.7\n",
    "        )\n",
    "        return response.choices[0].message.content.strip()\n",
    "    except Exception as e:\n",
    "        return f\"⚠️ Error: {e}\"\n",
    "\n",
    "# --- Output ---\n",
    "if st.button(\"Generate Plan\"):\n",
    "    if user_input:\n",
    "        with st.spinner(\"Creating your plan...\"):\n",
    "            output = generate_response(user_input)\n",
    "            st.success(\"Here's your personalized fitness plan!\")\n",
    "            st.write(output)\n",
    "    else:\n",
    "        st.warning(\"Please enter your fitness goal first.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f79e6e3-6655-4508-8393-58734275b7d3",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
