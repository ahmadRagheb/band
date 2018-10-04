function myMap() {
  const myCenter = new google.maps.LatLng(41.878114, -87.629798);
  const mapProp = {
    center:myCenter,
    zoom:12,
    scrollwheel:false,
    draggable:false,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  const map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
  const marker = new google.maps.Marker({
    position:myCenter
  });
  marker.setMap(map);
}
