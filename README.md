# Rasa ChatBot

Amandine Vallée - Maël Lucas - Martin Devreese (IA - promo 2022)

# Features

This rasa chatbot helps you find a random song produced by the artist of your choice. It uses 
the [spotify API](https://developer.spotify.com/documentation/web-api/) to fetch a song.
Here are some examples 

## Run the chatbot
To run the chatbot, open a shell at the root directory and run:
```cmd
rasa run actions
```
Then, in a new shell still at root dir, run:
```cmd
rasa shell -m './models/music_bot.tar.gz'
```

## Train the model 
To train the bot and overwrite current model, run:
```cmd
rasa train --fixed-model-name music_bot
```
## Examples
### Happy path example

```diff
Your input ->  Hello
+ Hey! I'm a music bot!
Your input ->  Play me some song then!
+ Give me an artist and I'll play one of its songs :D
Your input ->  Muse
+ Let's go for some Muse related songs ;)
+ Here is Uprising by Muse
+ Did that help you?
Your input ->  Yes! a lot
+ Bye
```

## Unhappy path example

```diff
Your input ->  Hey
+ Hey! I'm a music bot!
Your input ->  I don't like music
+ I'm so sorry, music is my only purpose. Plz go complain to the devs
+ Bye
```