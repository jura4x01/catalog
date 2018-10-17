function point2fields(event){
    $('#id_latitude').val(event.feature.geometry.y);
    $('#id_longitude').val(event.feature.geometry.x);
}
function fields2point(event){
    var wkt = "SRID=4326;POINT(" + $('#id_longitude').val() + " " + $('#id_latitude').val() + ")";
    $('#id_point').val(wkt);
    var admin_geom = geodjango_point.read_wkt(wkt);
    geodjango_point.write_wkt(admin_geom);
    geodjango_point.layers.vector.addFeatures([admin_geom]);
    geodjango_point.map.zoomToExtent(admin_geom.geometry.getBounds());
    geodjango_point.map.zoomTo(12);
}
$( document ).ready(function() {
    geodjango_point.layers.vector.events.on({"featuremodified": point2fields});
    geodjango_point.layers.vector.events.on({"featureadded": point2fields});

    $('#id_latitude, #id_longitude').change(fields2point);
});