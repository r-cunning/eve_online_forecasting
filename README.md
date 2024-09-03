### EVE Online Market Forecasting

Welcome to the EVE Online Market Forecasting respository. This is a hobby project which, in conjunction with my EVE Online Database Repository, is aimed at developing my database management, machine learning engineering and data science skills outside of my PhD work. 
EVE Online is a massively multiplayer online roleplaying game (MMORPG) developed by CCP with a focus on complex player-driven markets and industrial activity. The game's structure, coupled with the public availability of rich historical data, makes it ideal for the study of a simulated economy.
My aim for this project is to apply statistical techniques to player activity data to identify opportunities within the game's market.

To begin with I am focusing on implementing the data storage and loading pipeline (see the eve_online_market_database repository). As an initial proof of concept I am training a temporal fusion transformer model to forecast prices using simple features such as the number of items/ships destroyed in combat, faction warfare statistics and seasonality.
Ultimately I aim to add orderbook and market impact analysis to inform positioning when making buy or sell orders.
