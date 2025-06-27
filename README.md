
Local LLM Chatbot – Project: llmsetup


Run a private, local language model using Python and a quantized .gguf model.
No internet access or GUI required after setup.

------------------------------
Prerequisites (One-Time Setup)
------------------------------

1. Install Python 3.10+ (64-bit)
   - Download from: https://www.python.org/downloads/
   - During installation, check the box: "Add Python to PATH"

2. Enable Long File Path Support (Required for llama-cpp-python)

Option A: CMD Method (requires Administrator)

    reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f

Then restart your computer.

Option B: GUI Method

    1. Press Windows+R → type: gpedit.msc → press Enter  
    2. Navigate to:  
       Local Computer Policy >  
       Computer Configuration >  
       Administrative Templates >  
       System >  
       Filesystem  
    3. Double-click: "Enable Win32 long paths"  
    4. Set it to "Enabled" → click OK  
    5. Restart your computer

------------------------------
Step 1. Create Project Folder
------------------------------

    mkdir llmsetup
    cd llmsetup

------------------------------
Step 2. Create and Activate Virtual Environment
------------------------------

    python -m venv venv
    venv\Scripts\activate

------------------------------
Step 3. Install llama-cpp-python
------------------------------

    pip install llama-cpp-python

------------------------------
Step 4. Download GGUF Model
------------------------------

Option A: Using command line

    curl -L -o mistral.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf

Option B: Use a web browser

    https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF

Download the file:

    mistral-7b-instruct-v0.2.Q4_K_M.gguf

Then move it to this folder.

------------------------------
Step 5. Create Python Chat Script
------------------------------

    notepad chat.py

Paste this into the file:

    from llama_cpp import Llama

    llm = Llama(model_path="mistral-7b-instruct-v0.2.Q4_K_M.gguf", n_ctx=2048, n_threads=8, verbose=False)

    while True:
        prompt = input("You: ")
        print("Assistant:", llm(f"You are a helpful assistant.\nUser: {prompt}\nAssistant:", max_tokens=200, stop=["User:", "Assistant:"])["choices"][0]["text"].strip())

Save and close the file.

------------------------------
Step 6. Run the Chatbot
------------------------------

    python chat.py


------------------------------
To Run Again Later
------------------------------

1. Open CMD
2. Navigate to the project folder:

       cd path\to\llmsetup

3. Activate the virtual environment:

       venv\Scripts\activate

4. Start the chatbot:

       python chat.py
