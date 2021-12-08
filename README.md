# Rasa Open Source Chatbot

An introduction to chatbots with the rasa NLU library.
The pretrained chatbot is capable of giving a song from an artist you like.

## Chat with the bot
To run the chatbot, open a shell at the root directory and run:
```cmd
> rasa run actions
```
Then, in a new shell still at root dir, run:
```cmd
> rasa shell -m './models/music_bot.tar.gz'
```

## Train the model 
To train the bot and overwrite current model, run:
```cmd
> rasa train --fixed-model-name music_bot
```
