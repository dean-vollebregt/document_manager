async function getFilesAndS3Links() {

    const path = '/document';

    const headers = {};

    const body = {
        'operation': 'read_file_metadata',
    };

    return await apiGateway(path, headers, body);
}

async function createS3Object(base64String, fileName) {

    const path = '/document';

    const headers = {};

    const body = {
        "operation": "upload_file",
        "fileName": fileName,
        "fileData": base64String,
    };

    return await apiGateway(path, headers, body);
}

async function setMetadata(metadata) {

    const path = '/document';

    const headers = {};

    const body = {
        "operation": "store_file_metadata",
        "metadata": metadata
    };

    return await apiGateway(path, headers, body);
}

async function deleteFileMetadata(title) {

    const path = '/document';

    const headers = {};

    const body = {
        "operation": "delete_file_metadata",
        "title": title
    };

    return await apiGateway(path, headers, body);
}

async function deleteS3Object(fileName) {

    const path = '/document';

    const headers = {};

    const body = {
        "operation": "delete_file",
        "fileName": fileName
    };

    return await apiGateway(path, headers, body);
}