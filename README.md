# DjangoApiWithPrediction  
A Django Api project to do prediction to know if an article will be popular or not.  

DataSet : https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity  

To start the django project :  
>cd MyDjangoApi  
>python manage.py runserver  

You can now go to http://127.0.0.1:8000/api/alldata to see the data  
Or http://127.0.0.1:8000/api/data/5 to see the specific data with id=5  

Our prediction has around 70% of success  

To test the prediction you can use Postman and do a request Post within the column "popularity" and that will return you the data with the predicted popularity.  
Exemple of body to do the Post request :   
```
{
"url":"http:\/\/mashable.com\/2013\/01\/07\/apple-40-billion-app-downloads\/","timedelta":731.0,"n_tokens_title":9.0,"n_tokens_content":211.0,"n_unique_tokens":0.5751295307,
"n_non_stop_words":0.9999999916,"n_non_stop_unique_tokens":0.6638655406,"num_hrefs":3.0,"num_self_hrefs":1.0,"num_imgs":1.0,
"num_videos":0.0,"average_token_length":4.3933649289,"num_keywords":6.0,"data_channel_is_lifestyle":0.0,"data_channel_is_entertainment":0.0,
"data_channel_is_bus":1.0,"data_channel_is_socmed":0.0,"data_channel_is_tech":0.0,"data_channel_is_world":0.0,"kw_min_min":0.0,"kw_max_min":0.0,
"kw_avg_min":0.0,"kw_min_max":0.0,"kw_max_max":0.0,"kw_avg_max":0.0,"kw_min_avg":0.0,"kw_max_avg":0.0,"kw_avg_avg":0.0,
"self_reference_min_shares":918.0,"self_reference_max_shares":918.0,"self_reference_avg_sharess":918.0,"weekday_is_monday":1.0,"weekday_is_tuesday":0.0,
"weekday_is_wednesday":0.0,"weekday_is_thursday":0.0,"weekday_is_friday":0.0,"weekday_is_saturday":0.0,"weekday_is_sunday":0.0,
"is_weekend":0.0,"LDA_00":0.2177922885,"LDA_01":0.033334457,"LDA_02":0.0333514249,"LDA_03":0.0333335358,"LDA_04":0.6821882937,
"global_subjectivity":0.7022222222,"global_sentiment_polarity":0.3233333333,
"global_rate_positive_words":0.0568720379,"global_rate_negative_words":0.009478673,"rate_positive_words":0.8571428571,
"rate_negative_words":0.1428571429,"avg_positive_polarity":0.4958333333,"min_positive_polarity":0.1,"max_positive_polarity":1.0,
"avg_negative_polarity":-0.4666666667,"min_negative_polarity":-0.8,"max_negative_polarity":-0.1333333333,"title_subjectivity":0.0,
"title_sentiment_polarity":0.0,"abs_title_subjectivity":0.5,"abs_title_sentiment_polarity":0.0
}
```

This project has been done in collaboration with an ESILV student Niels Lorgnet
