**An awesome source code for a basic community manager Discord bot**

**Requirements:**
* `Python 3.11.2` [Download](https://www.python.org/)

**Usage:**
* `[1]` Clone the repo:
  ```bash
  git clone https://github.com/Reim-developer/Awesome-Discord-Bot.git
  ```
* `[2]` Then, go to **Awesome-Discord-Bot** via:
  ```bash
  cd Awesome-Discord-Bot
  ```

* `[3]` Check the **requirements.txt** file and install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

* `[4]` Config bot
    * Create a **.env** file from the template file **.env.example**:
    ```bash
    cp .env.example .env
    ```
    * Open the **.env** file and replace the following values:
    ```env
    TOKEN=YOUR_TOKEN_BOT_HERE
    BOT_PREFIX=YOUR_BOT_PREFIX_HERE
    CHANNEL_ID=YOUR_CHANNEL_ID_HERE
    ```

* `[5]` Finally, run `main.py`
  ```bash
  python3 main.py
  ```