jQuery(document).ready(function ($) {
    $(".slider-img").on("click", function () {
      $(".slider-img").removeClass("active");
      $(this).addClass("active");
    });
  });

document.addEventListener('DOMContentLoaded', function () {
    const sliderImages = document.querySelectorAll('.slider-img');

    sliderImages.forEach(img => {
        img.addEventListener('click', function () {
            // Hide details of all other slider images
            sliderImages.forEach(otherImg => {
                if (otherImg !== img) {
                    otherImg.querySelector('.details').style.display = 'none';
                }
            });

            // Toggle the visibility of the clicked slider image's details
            const details = img.querySelector('.details');
            if (details.style.display === 'block') {
                details.style.display = 'none';
            } else {
                details.style.display = 'block';
            }
        });
    });
});
