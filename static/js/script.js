function updateSubcategories() {
    var category = document.getElementById('category').value;
    var subcategories = categories[category].subcategories;

    var subcategorySelect = document.getElementById('subcategory');
    subcategorySelect.innerHTML = '';
    for (var i = 0; i < subcategories.length; i++) {
        var option = document.createElement('option');
        option.value = subcategories[i].id;
        option.text = subcategories[i].name;
        subcategorySelect.appendChild(option);

    }
};

window.onload = updateSubcategories;
document.getElementById('category').addEventListener('change', updateSubcategories);