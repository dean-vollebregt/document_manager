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
        "operation": "createS3Object",
        "fileName": fileName,
        "fileData": base64String,
    };
    debugger;
    return await apiGateway(path, headers, body);
}

async function setFileOrHyperLinkMetadata(metadata, accessToken, cognitoToken) {

    const path = '/document';

    const headers = {
        'Authorization': cognitoToken
    };
    const body = {
        "operation": "setFileOrHyperLinkMetadata",
        "metadata": metadata,
        "accessToken": accessToken
    };

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

module.exports = {
    getFilesAndHyperlinks,
    createS3Object,
    setFileOrHyperLinkMetadata,
    deleteFileAndHyperlinkMetadata,
    deleteS3Object
};