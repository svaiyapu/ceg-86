//
// Mother land is in center
//
var INDIA = new google.maps.LatLng(20.5936840,78.9628800);

//
// the proverbial main
//
function initialize() {
    var mapOptions = {
                        zoom: 2,
                        center: INDIA,
                        mapTypeId: google.maps.MapTypeId.ROADMAP
                        };
    var map = new google.maps.Map(document.getElementById("map_canvas"),
                                    mapOptions);
    var locs = locations();
    hookem(map, locs);
}

//
// Member object
//
function Member(fn, ln, dpt, sec, faddr, lat, lng) {
    this.fn = fn;
    this.ln = ln;
    this.dpt = dpt;
    this.sec = sec;
    this.faddr = faddr;
    this.lat = lat;
    this.lng = lng;
}
function getName() {
    return this.fn + " " + this.ln;
}
Member.prototype.getName = getName;

function locations() {
    var locs = new Array();
    for (var i = 0; i < members.length; i++) {
        if (locs[members[i].faddr] == null)
            locs[members[i].faddr] = new Array();
        locs[members[i].faddr].push(members[i]);
    }
    return locs;
}

// 
// setup markers, infowindows and hookem
//
function hookem(map, locs) {
    for (key in locs) {
        var mems = locs[key]; 
        var latlng = new google.maps.LatLng(mems[0].lat, mems[0].lng);

        // set up a infowindow
        var content = "<div style=\"font-famly:Georgia, serif; font-size:12px\">";
        content += "<h3>" + key + "</h3>";
        content += "<table style=\"border-collapse:collapse\">";
        for (var i=0; i<mems.length; i++) {
            content += "<tr>";
            content += "<td><strong>" + mems[i].getName() + "</strong></td>";
            content += "<td><em>" + mems[i].dpt + "</em></td>";
            if (mems[i].sec != null)
                content += "<td><em>" + mems[i].sec + "</em></td>";
            content += "</tr>";
        } 
        content += "</table>";
        content += "</div>";

        var marker = new google.maps.Marker({
                        position: latlng,
                        map: map,
                        title: key,
                        content: content
                    });
        var iw = new google.maps.InfoWindow({ content: content });

        // hookem
        google.maps.event.addListener(marker, 'click', function() {
            iw.setContent(this.content);
            iw.open(map, this);
            });
    }
}

var members = new Array();
// Emit member instantiations here
members.push(new Member("A","Aaivu","Civil",null,"Chennai, Tamil Nadu, India",13.0604220,80.2495830));
members.push(new Member("ANBARASU","B","Mechanical","A&B","India",20.5936840,78.9628800));
