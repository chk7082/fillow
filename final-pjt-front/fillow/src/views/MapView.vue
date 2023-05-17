<template>
  <div>
    <gmap-map
        :zoom="3"    
        :center="center"
        style="width:100%;  height: 855px;"
      >
      <gmap-marker
        :key="index"
        v-for="(m, index) in locationMarkers"
        :position="m.position"
      ></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
export default {
  name: "MapView",
  data() {
    return {
      center: { lat: 37.5642135, lng: 127.0016985 },
      locationMarkers: [
        {
          position: { lat: 37.5642135 ,lng: 127.0016985 },
        }
      ],
      locPlaces: [],
      existingPlace: null
    };
  }, 
};
</script>