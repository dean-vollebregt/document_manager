async function getFilesAndHyperlinks() {

    const path = '/admin';

    const headers = {
        'Authorization': cognitoToken
    };

    const body = {
        'operation': 'getFilesAndHyperlinks',
        'accessToken': accessToken
    };

    return await apiGateway(path, headers, body);
}

async function createS3Object(base64String, fileName) {

    const path = '/document';

    const headers = {};

    const body = {
        "operation": "create_s3_object",
        "fileName": fileName,
        "fileData": base64String,
    };

    return await apiGateway(path, headers, body);
}

async function setMetadata(metadata) {

    const path = '/document';

    const headers = {};

    const body = {
        "operation": "set_meta_data",
        "metadata": metadata
    };
    debugger
    return await apiGateway(path, headers, body);
}

async function deleteFileAndHyperlinkMetadata(selectedRowTitle, accessToken, cognitoToken) {

    const path = '/document';

    const headers = {
        'Authorization': cognitoToken
    };

    const body = {
        "operation": "deleteFileAndHyperlinkMetadata",
        "title": selectedRowTitle,
        "accessToken": accessToken
    };

    return await apiGateway(path, headers, body);
}

async function deleteS3Object(fileName, accessToken, cognitoToken) {

    const path = '/document';

    const headers = {
        'Authorization': cognitoToken
    };
    const body = {
        "operation": "deleteS3Object",
        "fileName": fileName,
        "accessToken": accessToken
    };

    return await apiGateway(path, headers, body);
}