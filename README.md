# stælker

> “You can't be like pop stars, but you can be part of their story. You can be their fan.”
― Simon Cheshire, Plastic Fantastic

The event-monitoring service between fans and artists/celebrity/brands on Twitter. 

Built for onlyfæns (decentralized fan-service) which we were supposed to build for [æternity's humandefihaeck](https://humandefihaeck.devpost.com/).


<p align="center">
  <br>
  <img src="https://i.postimg.cc/2yS9VXVj/only-faens.jpg"/>
  <br>
</p>

This service uses the [Twitter v1 Streaming API](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/overview) for following a list of celebrities and their tweets & re-tweets on Twitter. It also calculates the ∆ (`delta`) in seconds between the celebrity's tweet & fan's retweet to reward the fan's loyalty.

Then it pushes the collected information into an instance of [RabbitMQ](https://www.rabbitmq.com/), the core-backend & æternity's oracle services can use this information to actually reward the fans on the æternity blockchain.


## Concept around Only Fæns

simply put: fans retweet artist/celebrity/brands content and earn fan-loyal-social tokens on the blockchain.

### Use Cases:

1. distribute the limited amount of social tokens exponentially over duration (faster the fan retweets, the more he gets rewarded, thus non-linearity)

2. These artist/celebrity/brands after getting verified status, can list these social-tokens on cryptocurrency exchanges.

3. fans who collect these social-tokens can request for fan services (in exchange for those social tokens) like: 
    * birthday wishes
    * twitter shoutout
    * purchase merch
    * personalized merch, gifts
    * polls
    * purchase tickets for matches / conference / concerts. 
    
since fan tokens are limited artist/celebrity/brands need to do services to get the tokens back from fans, else do a [crypto-buyback](https://www.investopedia.com/terms/b/buyback.asp) straight from exchanges.

if fans don't have enough fan-tokens for that fan-service they can purchase token/ae from exchange. if fans get bored they can convert it to ae tokens and then fiat currency too.

## y tho?

As you might have guessed this opens up a whole new platform of investing/speculating on a fandom. 

Freddie Mercury died in 1991 but has a twitter account with ~272k followers. Fans never die.


<p align="center">
  <br>
  <img src="https://i.postimg.cc/90FhBpNz/MV5-BMTA2-NDc3-Njg5-NDVe-QTJe-QWpw-Z15-Bb-WU4-MDc1-NDcx-NTUz-V1.jpg"/>
  <br>
  <em>image belongs to imdb</em>
  <br>
  <br>
</p>


## Hypothetical Example Use Cases for these fan-social-tokens

* [Nike](https://www.nike.com/in/) giving shoutout for marathon runners for **$NIKE** tokens.
* [Alia Bhatt](https://www.instagram.com/aliaabhatt/?hl=en) wishing her fan on Birthday for **$BHATT** tokens.
* [Thirupathi Perumal](https://en.wikipedia.org/wiki/Venkateswara_Temple,_Tirumala) giving direct dharishanam/dharshan using **$TIRUMALA** tokens.
* [BTS](https://www.instagram.com/bts.bighitofficial/) fans buying concert tickets for **$BTS** tokens.
* [MKBHD](https://www.youtube.com/user/marquesbrownlee) fans buying MKBHD shirts for **$MKBHD** tokens.
* [Virat Kohli](https://en.wikipedia.org/wiki/Virat_Kohli) signing cricket bats and shipping it for fans in return for **$KOHLI** tokens.
