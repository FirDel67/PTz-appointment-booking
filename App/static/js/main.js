function loadTranslation(language) {
    const translations = {
        'fr': '../../static/translations/fr.json',
        'sw': '../../static/translations/sw.json',
        'rundi': '../../static/translations/rundi.json',
        'en': '../../static/translations/en.json'
    };

    const url = translations[language];
    if (url) {
        fetch(url)
            .then(response => response.json())
            .then(data => applyTranslations(data))
            .catch(error => console.error("Error loading translation file:", error));
    } else {
        resetToEnglish(); // If English, no need to load a file
    }
}

// Function to apply translations to the page
function applyTranslations(data) {
    for (const key in data) {
        const elements = document.querySelectorAll(`[data-translate="${key}"]`);
        elements.forEach(element => {
            element.textContent = data[key];
        });
    }
}

// Reset to English default
function resetToEnglish() {
    document.querySelectorAll('[data-translate]').forEach(element => {
        element.textContent = element.getAttribute('data-translate');
    });
}

// Event listener for language change
document.getElementById('language-selector').addEventListener('change', (event) => {
    loadTranslation(event.target.value);
});

// Initially load translations for the selected language
loadTranslation('en'); // Set default language to English

