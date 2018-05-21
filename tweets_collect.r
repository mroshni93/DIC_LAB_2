library (twitteR)
api_key <- "46RnSDyQPCPLlvtVp9h2dnFI8"
api_secret <- "lDDThVLuLdz6Y8peK4ynDwVi77YRwx1CHNXCnXwSKYYHtttka6"
token <- "961771590252974080-JPHTkHB78un85PmkdiDEOSM3nrZzYco"
token_secret <- "V0NKiqmG3znLabn4Vh1rV87hU4xOBQ0IjCBCby0dRCoGE"
setup_twitter_oauth(api_key, api_secret, token, token_secret)
tweets <- searchTwitter("royal wedding OR #royalwedding", n = 2000, lang = "en")
tweets.df <-twListToDF(tweets)
write.csv(tweets.df, "E:/Buffalo/Semester_2/CSE_587_Data_Intensive_Computing/Lab/2/Part 2/Tweets/Lab_2/day_2.csv")