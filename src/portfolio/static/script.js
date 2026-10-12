function copyToClipboard(text, shouldWarn = true) {
    navigator.clipboard.writeText(text).then(r => {
        if (shouldWarn) {
            alert(`Copied "${text}" to clipboard`);
        }
    });
}