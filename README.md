[Monica](https://github.com/monicahq/monica) is a really neat tool that allows you to manage your personal relationships better by logging calls, birthdays, and other important imformation.

This script adds OpenAI suggestions to your Monica UI to help you ask good questions and deepen your relationships even further.


Add a call:

![jewelry-store](./images/jewelry-store.png)


This script runs the call log content against OpenAI, asking for suggestions and follow-up questions, and then updates the call with the response:

![jewelry-gpt-response](./images/jewelry-gpt-response.png)


Other examples
![gpt-response](./images/gpt-response-mom.png)



Setup
====

configue the `.env` file with your API keys



Run
====

`python3 main.py`

todo: check if there's an on-save hook for calls and run this automatically