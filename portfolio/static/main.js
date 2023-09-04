var imageContainer = document.getElementById('imageContainer');
        var images = imageContainer.getElementsByTagName('img');

        function checkImagesRendered() {

            for (var i = 0; i < images.length; i++) {
                var image = images[i];
                var allImagesRendered = true;
                var masonryInstance = $('#imageContainer').data('masonry');
                masonryInstance.layout();

                if (image.complete && (image.naturalWidth === 0 || image.naturalHeight === 0)) {
                    allImagesRendered = false;
                    break;
                }
            }
        }
        window.onload = checkImagesRendered;