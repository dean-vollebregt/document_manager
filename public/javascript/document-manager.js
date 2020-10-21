async function onPageLoad() {
    try {

        hideLoadingDiv()
        showManageS3ContentPanel()

        let allItemsArray = await getFilesAndHyperlinks(accessToken, cognitoToken);
        renderFilesAndHyperlinks(allItemsArray.Items);
        //hideLoadingDiv()
        setTimeout(showManageS3ContentPanel, 500);
    } catch (err) {
        console.log(err)
    }
}

function renderFilesAndHyperlinks(allItemsArray){

    document.getElementById("tableBody").innerHTML ='';
    document.getElementsByTagName("FORM")[0].reset();

    allItemsArray.sort(function (a, b) {
        return (b.title > a.title) ? -1 : 1;
    });

    allItemsArray.forEach(function(item){
        let individualItemRow =
         `<tr>
            <td class="title">${item.title.S}</td>
            <td class="description">${item.description.S}</td>
            <td class="reference"><a href="${item.reference.S}">${item.reference.S}</a></td>
            <td class="date_created">${item.date_created.S}</td>
            <td class="delete" id="${item.fileName.S}"><button onclick="onDeleteOrHyperlink(this.parentElement.parentNode)">Delete</button></td>
         </tr>` ;

        document.getElementById("tableBody").innerHTML += individualItemRow
    });
}

function hideLoadingDiv(){
    document.getElementById('loadingDiv').classList.add('d-none');
}

function showManageS3ContentPanel() {
    document.getElementById('manageS3ContentPanel').classList.remove('d-none');
}

async function validateForm() {

    let title = document.getElementById("title").value;
    let description = document.getElementById("description").value;

    if(title === "" || description === "") {
        alert('Title or Description is incomplete');
    }
    else {
        return await setStorageType();
    }
}

async function setStorageType(){

    try {
        let base64String = await getBase64();
        let pdfLocation  = await createS3Object(base64String[0], base64String[1], accessToken, cognitoToken);
        let metadata = await fileOrHyperLinkDataMetadata(pdfLocation);
        let response = await setFileOrHyperLinkMetadata(metadata, accessToken, cognitoToken);
        let allItemsArray = await getFilesAndHyperlinks(accessToken, cognitoToken);
        renderFilesAndHyperlinks(allItemsArray.Items);

    } catch(err){
        console.log(error)
    }
}

async function getBase64() {

    let fileToLoad = document.getElementById("uploadFile").files[0];
    let fileName = fileToLoad.name;
    let fileReader = new FileReader();

    return new Promise((resolve, reject)=>{
        fileReader.onload = function(){
            let base64String = fileReader.result.split(',')[1];
            return resolve([ base64String, fileName ]);
        };
        fileReader.readAsDataURL(fileToLoad);
    });
}

function fileOrHyperLinkDataMetadata(pdfLocation) {

    let metadata =  {
        "title": document.getElementById("title").value,
        "description": document.getElementById("description").value,
        "reference": pdfLocation.Location,
        "date_created": new Date(Date.now()).toLocaleDateString(),
        "fileName": (fileOrHyperlink === 'File' ? document.getElementById("uploadFile").files[0].name : "none")
    };

    return metadata
}

async function onDeleteOrHyperlink(selectedRow) {

    let selectedRowTitle = selectedRow.getElementsByClassName("title")[0].innerText;
    let resourceType = selectedRow.getElementsByClassName("type")[0].innerText;
    let fileName = selectedRow.getElementsByClassName("delete")[0].id;

    try {
        await deleteFileAndHyperlinkMetadata(selectedRowTitle, accessToken, cognitoToken);
        if (fileName !== "none") await deleteS3Object(fileName, accessToken, cognitoToken);
        selectedRow.innerHTML = '';
    } catch (err) {
        console.log(err)
    }
}

document.addEventListener("DOMContentLoaded", function(){
    onPageLoad();
});

