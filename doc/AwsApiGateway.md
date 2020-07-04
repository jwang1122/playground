# AWS API Gateway

[Web URL](https://us-east-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-2#/environments)
* Create Lambda
    - Lambda
    - Create function > Python 3.8
* API Gateway
    - Create API
    - HTTP API > Build > Add Integration > Integration: Lambda > select lambda above
    - API name: <name>
    - Any: Get > Resource Path: <table> > Integration target: <Lambda function name>
    - Stage Name: $default > [Next] > [Create]
    - 

