function load_doctor(){
    var url = $("#application_form").attr("data-doctor-url");
    var speciality = $("#id_speciality").val();
    var divisionId = $("#division").val();
    var district = $("#district").val();
    var upazila = $("#upazila").val();

    $.ajax({
        url: url,
        data: {
        'speciality': speciality,
        'division': divisionId,
        'district': district,
        'upazila': upazila,
        },
        success: function (data) {
        $("#id_doctor").html(data);
        }
    });
};


$("#id_speciality").change(function () {
    load_doctor();
});
$("#division").change(function () {
    load_doctor();
});
$("#district").change(function () {
    load_doctor();
});
$("#upazila").change(function () {
    load_doctor();
});

