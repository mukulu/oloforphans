function dismissPopupAndReload(win) {
    document.location.reload();
    win.close();
};
function dismissRelatedImageLookupPopup(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt) {
    var name = windowname_to_id(win.name);
    var img_name = name + '_thumbnail_img';
    var txt_name = name + '_description_txt';
    var elem = document.getElementById(name);
    document.getElementById(name).value = chosenId;
    document.getElementById(img_name).src = chosenThumbnailUrl;
    document.getElementById(txt_name).innerHTML = chosenDescriptionTxt;
    win.close();
};
function dismissRelatedFolderLookupPopup(win, chosenId, chosenName) {
    var id = windowname_to_id(win.name);
    var id_name = id + '_name';
    document.getElementById(id).value = chosenId;
    document.getElementById(id_name).innerHTML = chosenName;
    win.close();
};
