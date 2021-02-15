jQuery(function ($) {
    $(".fadetoggle").on("click", function () {
        $(".form").fadeToggle(10).css('display', 'inline');
    });
    $(".reply").on("click", function () {
        console.log(this);
        var counter = $(this).data('counter');
        console.log(counter);
        $("#multiCollapseExample" + counter).fadeToggle(10).css('display', 'inline');
        // console.log("Lage 6");
    });
    $(".hide_comment").hide();
    $(".view_more").on("click", function () {
        $(".hide_comment").toggle();
    });
    $(function () {
        $.fn.toggleText = function (text1, text2) {
            return this.each(function () {
                var self = $(this);
                if (self.text() == text1)
                    self.text(text2);
                else
                    self.text(text1);
            });
        };

        $("#view_more").click(function () {
            $(this).toggleText('Hide', 'View More');
        });
    });


});