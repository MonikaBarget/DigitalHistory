var fieldName = "title";
var fieldID = Zotero.ItemFields.getID(fieldName);
var s = new Zotero.Search();
s.libraryID = ZoteroPane.getSelectedLibraryID();
s.addCondition(fieldName, 'contains', 'Elektronisk resurs');
var ids = await s.search();
if (!ids.length) {
    return "No items found";
}
await Zotero.DB.executeTransaction(async function () {
    for (let id of ids) {
        let item = await Zotero.Items.getAsync(id);
        let mappedFieldID = Zotero.ItemFields.getFieldIDFromTypeAndBase(item.itemTypeID, fieldName);
        let fieldID = mappedFieldID || fieldID;
        item.setField(fieldID, item.getField(fieldID).replace(/Elektronisk resurs/g, ''));
        await item.save({
            skipDateModifiedUpdate: true
        });
    }
});
return ids.length + " item(s) updated";
