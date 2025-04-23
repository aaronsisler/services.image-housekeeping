import json

import boto3


def handle_new_image(event, _context):
    print(event)

    ecr_client = boto3.client('ecr')

    image_details = event['detail']
    repository_name = image_details['repository-name']

    response = ecr_client.describe_images(
        repositoryName=repository_name
    )

    print(response)

    # Need to loop over the images and delete the ones that don't have imageTag as latest

    return {
        'statusCode': 200,
        'body': json.dumps(f'Images that are not the latest have been deleted from {repository_name}')
    }
