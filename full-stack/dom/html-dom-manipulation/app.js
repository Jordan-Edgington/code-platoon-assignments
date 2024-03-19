//logs alt text to console and replaces the image with the alt text
const showAlt = () => {
    imgs = document.getElementsByTagName("img")
    for (let i = imgs.length-1; i>=0; i--) {
        console.log(i);
        let img = imgs[i];
        console.log(img.alt)
        if (img.alt) {
            let altText = document.createTextNode(img.alt);
            img.parentNode.replaceChild(altText,img);
        }
    }
}