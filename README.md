# Whatstics

# Features

## Phase 1

### Summary

[Inspiration: Group Chat Summarizer](https://github.com/omer-go/group_chat_summarizer)

- ✅ Filter by date
- ✅ Summarize conversation
- ✅ Get links from conversation
- Categories of links


### Statistics

[Inspiration: Chatistics](https://chatistics.vercel.app/)

- Filter by date
- Get statistics from conversation
- General statistics such as
  - Total Days
  - Total Messages exchanged
  - Total Words exchanged
  - Total Media exchanged
  - Total Links exchanged
  - Total Emojis exchanged
- Statics by
  - year
  - month
  - day
  - hour
- Specific statistics such as
  - Most used emoji
  - Who sends more messages
  - Who sends more media
  - Who sends more links
  - Who sends more emojis
  - Most used words

## Next Phases

- Filter by user
- Get images from conversation


## Install Instructions

1. Copy the file .env.example to .env, then fill the variables with your own values.

## Run Instructions

1. Export WhatsApp chat (without media) to a .txt file
2. Save this file in the `history` folder
3. Change the hyperparameters in the `/src/summarizer.ipynb` file
   1. The path to the historyfolder: `FILE_PATH`
   2. The path to the summary folder: `SUMMARY_PATH`
   3. The start and end dates: `START_DATE` and `END_DATE`
   4. The LLM model: LLM_PROVIDER `OPENAI` or `GOOGLE`. We recommend using "OPENAI" because it generates better results.
4. Run the file and enjoy the results!
