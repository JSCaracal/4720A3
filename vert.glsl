in vec3 position;
in vec3 normal;
uniform float scale;
uniform vec3 center;
uniform float aspect;

out vec3 fragColor;

void main(){
    vec3 pos = position-center
    gl_Position = vec4(pos * scale, 1.0);
    fragColor = color;
}