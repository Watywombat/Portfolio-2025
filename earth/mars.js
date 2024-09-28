import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.161/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.161/examples/jsm/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create stars
const createStarfield = () => {
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(2000 * 3);

    for (let i = 0; i < positions.length; i++) {
        positions[i] = (Math.random() - 0.5) * 2000; // Random positions
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const material = new THREE.PointsMaterial({ color: 0xffffff });
    return new THREE.Points(geometry, material);
};
const stars = createStarfield();
scene.add(stars);

// Mars setup
const geometry = new THREE.SphereGeometry(1, 32, 32);
const loader = new THREE.TextureLoader();
const marsMaterial = new THREE.MeshPhongMaterial({
    map: loader.load('threejs-earth-main/earth/textures/marsmap1k.jpg'), // Mars texture
});
const marsMesh = new THREE.Mesh(geometry, marsMaterial);
scene.add(marsMesh);

// Lighting
const sunLight = new THREE.DirectionalLight(0xffffff, 1);
sunLight.position.set(5, 5, 5);
scene.add(sunLight);
const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);

// Camera position
camera.position.z = 5;

// Orbit Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Animation loop
function animate() {
    requestAnimationFrame(animate);

    // Rotate Mars
    marsMesh.rotation.y += 0.01;

    // Update controls
    controls.update();
    renderer.render(scene, camera);
}

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

animate();
