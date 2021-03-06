async function onPageLoad() {
    try {
        hideLoadingDiv()
        showManageS3ContentPanel()
        let allItemsArray = await getFilesAndS3Links();
        renderFilesAndS3links(allItemsArray);
        //hideLoadingDiv()
        setTimeout(showManageS3ContentPanel, 500);
    } catch (err) {
        console.log(err)
    }
}

function renderFilesAndS3links(allItemsArray){

    document.getElementById("tableBody").innerHTML ='';
    document.getElementsByTagName("FORM")[0].reset();

    allItemsArray.sort(function (a, b) {
        return (b.title > a.title) ? -1 : 1;
    });

    allItemsArray.forEach(function(item){
        let individualItemRow =
         `<tr>
            <td class="title">${item.title}</td>
            <td class="description">${item.description}</td>
            <td class="reference"><a href="${item.reference}">${item.reference}</a></td>
            <td class="date_created">${item.date_created}</td>
            <td class="delete" id="${item.fileName}"><button onclick="deleteFile(this.parentElement.parentNode)">Delete</button></td>
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
        return await storeItem();
    }
}

async function storeItem(){

    try {
        let base64String = await getBase64();
        let pdfLocation  = await createS3Object(base64String[0], base64String[1]);
        let metadata = await fileMetadata(base64String[1]);
        let response = await setMetadata(metadata);
        let allItemsArray = await getFilesAndS3Links();
        renderFilesAndS3links(allItemsArray);

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

function fileMetadata(fileName) {

    let metadata =  {
        "title": document.getElementById("title").value,
        "description": document.getElementById("description").value,
        "reference": "https://document-manager-demo.s3-ap-southeast-2.amazonaws.com/" + fileName,
        "date_created": new Date(Date.now()).toLocaleDateString(),
        "fileName": fileName
    };

    return metadata
}

async function deleteFile(selectedRow) {

    let selectedRowTitle = selectedRow.getElementsByClassName("title")[0].innerText;
    let fileName = selectedRow.getElementsByClassName("delete")[0].id;

    try {
        await deleteFileMetadata(selectedRowTitle);
        await deleteS3Object(fileName);
        selectedRow.innerHTML = '';
    } catch (err) {
        console.log(err)
    }
}

document.addEventListener("DOMContentLoaded", function(){
    onPageLoad();
});

