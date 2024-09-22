# BizKnow

BizKnow is an AI-powered company intelligence tool that offers instant, semantic search across corporate data using OpenAI embeddings and Streamlit.

## Overview

BizKnow allows users to uncover insights, explore company information, and gain deep business knowledge using natural language queries. It's fast, accurate, and user-friendly.

This application uses an embeddings search pattern, which is excellent for:
* Identifying related items based on text descriptions
* Application portfolio rationalization - particularly in cases where data between companies or divisions is inconsistent

## How It Works

1. Documents are broken up into chunks of text. These chunks are converted to vectors using OpenAI's text embeddings and saved to a local Chroma vector database.
2. The user submits a question through the Streamlit interface.
3. The question is converted to a vector using OpenAI embeddings, then matched to the closest vectors in the database.
4. The content from the matching vectors is returned and displayed to the user.

## Project Structure

This application consists of three main files:

1. `streamlit_app.py`: The Streamlit front-end interface.
2. `embeddings_search_lib.py`: The supporting library for making calls to OpenAI API and managing the vector database.
3. `populate_collection.py`: A script to initialize and populate the vector database with company information.

## Setup and Installation

1. Clone this repository:
   ```
   git clone https://github.com/bdeva1975/BizKnow.git
   cd BizKnow
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Populate the vector database:
   ```
   python populate_collection.py
   ```

5. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

## Usage

Once the app is running, you can enter natural language queries about the company in the text input field. Click the "Search" button to retrieve relevant information from the vector database.

## Note

In a real-world scenario, you might want to use a persistent data store or a more robust vector database solution for larger datasets.
