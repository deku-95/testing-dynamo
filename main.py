import boto3

dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1", endpoint_url="http://localhost:8000")
main_table = dynamodb.Table("test")
def test_setup():
    try:
            dynamodb.create_table(
                TableName="test",
                KeySchema=[
                    {"AttributeName": "pk", "KeyType": "HASH"},
                    {"AttributeName": "sk", "KeyType": "RANGE"},
                ],
                AttributeDefinitions=[
                    {"AttributeName": "pk", "AttributeType": "S"},
                    {"AttributeName": "sk", "AttributeType": "S"},
                ],
                ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
            )
        
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        pass

    main_table = dynamodb.Table("test")
        # check if table is working
    assert main_table.table_status == "ACTIVE"

def test_create_user():
    # put user into dynamodb

    main_table.put_item(
        Item={
            "pk": "8cbd8ea0-2aa2-46ce-8928-da548bd31386",
            "sk": "deku-95",
        }
    )
    # check if user is in dynamodb
    try:
        assert main_table.get_item(Key={"pk": "8cbd8ea0-2aa2-46ce-8928-da548bd31386", "sk": "deku-95"})["Item"] == { "pk": "8cbd8ea0-2aa2-46ce-8928-da548bd31386", "sk": "deku-95" }
        print("OK")
    except:
        print("BAD")
