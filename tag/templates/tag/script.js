<script type="text/javascript">
var i=0;
var cl = {{ json_children_left|safe }};
var cr = {{ json_children_right|safe }};
var feature = {{ json_feature|safe }};
var predicted_movie = {{ json_predicted_movie|safe }};
var n_nodes = {{ n_nodes }};
var current_node = 0;

var question = "Do you want "+feature[0]+"?";
document.getElementById("question").innerHTML = question;

function myFunction_yes() {
    current_node = cr[current_node];
    if (feature[current_node] != "None") {
        question = "Do you want "+feature[current_node]+"?";
        document.getElementById("question").innerHTML = question;
        i=i+1;
    } else {
        document.getElementById("hdd").value = current_node;
        document.getElementById("answer_form").submit();
    }
}
function myFunction_no() {
    current_node = cl[current_node];
    if (feature[current_node] != "None") {
        question = "Do you want "+feature[current_node]+"?";
        document.getElementById("question").innerHTML = question;
        i=i+1;
    } else {
        document.getElementById("hdd").value = current_node;
        document.getElementById("answer_form").submit();
    }
}
document.getElementById("prediction").innerHTML = predicted_movie;

<!--document.write(cl);-->
</script>
