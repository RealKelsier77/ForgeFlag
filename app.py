import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Roblox FFlag Generator", layout="centered")

# Define the FFlag library (same as before, but in Python)
fflag_library = {
    "lowPing": [
        "\n".join([
            "FFlagNetworkPriority=true",
            "FFlagReducePingSpikes=true",
            "FFlagPingSmoothing=true",
            "FFlagFastNetworkMode=true",
            "FFlagLowPingOptimization1=true",
            "FFlagNetBufferSize=8192",
            "FFlagPacketCompression=true",
            "FFlagNetworkThrottling=false",
            "FFlagAsyncNetCalls=true",
            "FFlagPingInterval=50",
            "FFlagConnectionRetries=3",
            "FFlagNetQueueOptimize=true"
        ]),
        "\n".join([
            "FFlagNetworkPriority=true",
            "FFlagLowPingOptimization2=true",
            "FFlagPingSmoothing=true",
            "FFlagFastNetworkMode=true",
            "FFlagNetBufferSize=16384",
            "FFlagPacketCompression=true",
            "FFlagNetworkThrottling=false",
            "FFlagAsyncNetCalls=true",
            "FFlagPingInterval=40",
            "FFlagConnectionRetries=5",
            "FFlagNetQueueOptimize=true",
            "FFlagLowPingBoost=true",
            "FFlagNetLatencyCap=100"
        ]),
        "\n".join([
            "FFlagNetworkPriority=true",
            "FFlagReducePingSpikes=true",
            "FFlagPingSmoothing=true",
            "FFlagFastNetworkMode=true",
            "FFlagNetBufferSize=4096",
            "FFlagPacketCompression=true",
            "FFlagNetworkThrottling=false",
            "FFlagAsyncNetCalls=true",
            "FFlagPingInterval=60",
            "FFlagConnectionRetries=2",
            "FFlagNetQueueOptimize=true",
            "FFlagLowPingBoost=true"
        ]),
        "\n".join([
            "FFlagNetworkPriority=true",
            "FFlagLowPingOptimization1=true",
            "FFlagPingSmoothing=true",
            "FFlagFastNetworkMode=true",
            "FFlagNetBufferSize=12288",
            "FFlagPacketCompression=true",
            "FFlagNetworkThrottling=false",
            "FFlagAsyncNetCalls=true",
            "FFlagPingInterval=45",
            "FFlagConnectionRetries=4",
            "FFlagNetQueueOptimize=true",
            "FFlagLowPingBoost=true",
            "FFlagNetLatencyCap=80",
            "FFlagNetErrorCorrection=true"
        ]),
        "\n".join([
            "FFlagNetworkPriority=true",
            "FFlagReducePingSpikes=true",
            "FFlagPingSmoothing=true",
            "FFlagFastNetworkMode=true",
            "FFlagNetBufferSize=20480",
            "FFlagPacketCompression=true",
            "FFlagNetworkThrottling=false",
            "FFlagAsyncNetCalls=true",
            "FFlagPingInterval=55",
            "FFlagConnectionRetries=3",
            "FFlagNetQueueOptimize=true",
            "FFlagLowPingBoost=true",
            "FFlagNetLatencyCap=120"
        ])
    ],
    "highFPS": [
        "\n".join([
            "FFlagHighFPSBoost=true",
            "FFlagFrameRateUnlock=true",
            "FFlagVSyncOff=true",
            "FFlagRenderPriority=true",
            "FFlagFPSCapRemove=true",
            "FFlagDynamicFrameRate=true",
            "FFlagRenderThreadOptimize=true",
            "FFlagGPUFrameBuffer=2",
            "FFlagFrameQueueSize=3",
            "FFlagRenderBatchSize=16",
            "FFlagSyncRenderLoop=true",
            "FFlagFPSPriority=true"
        ]),
        "\n".join([
            "FFlagHighFPSBoost=true",
            "FFlagFrameRateUnlock=true",
            "FFlagVSyncOff=true",
            "FFlagRenderPriority=true",
            "FFlagFPSCapRemove=true",
            "FFlagDynamicFrameRate=true",
            "FFlagRenderThreadOptimize=true",
            "FFlagGPUFrameBuffer=4",
            "FFlagFrameQueueSize=2",
            "FFlagRenderBatchSize=32",
            "FFlagSyncRenderLoop=true",
            "FFlagFPSPriority=true",
            "FFlagHighFrameRateMode=true",
            "FFlagRenderThrottle=false"
        ]),
        "\n".join([
            "FFlagHighFPSBoost=true",
            "FFlagFrameRateUnlock=true",
            "FFlagVSyncOff=true",
            "FFlagRenderPriority=true",
            "FFlagFPSCapRemove=true",
            "FFlagDynamicFrameRate=true",
            "FFlagRenderThreadOptimize=true",
            "FFlagGPUFrameBuffer=3",
            "FFlagFrameQueueSize=4",
            "FFlagRenderBatchSize=24",
            "FFlagSyncRenderLoop=true",
            "FFlagFPSPriority=true",
            "FFlagHighFrameRateMode=true"
        ]),
        "\n".join([
            "FFlagHighFPSBoost=true",
            "FFlagFrameRateUnlock=true",
            "FFlagVSyncOff=true",
            "FFlagRenderPriority=true",
            "FFlagFPSCapRemove=true",
            "FFlagDynamicFrameRate=true",
            "FFlagRenderThreadOptimize=true",
            "FFlagGPUFrameBuffer=1",
            "FFlagFrameQueueSize=5",
            "FFlagRenderBatchSize=20",
            "FFlagSyncRenderLoop=true",
            "FFlagFPSPriority=true",
            "FFlagHighFrameRateMode=true",
            "FFlagRenderThrottle=false",
            "FFlagFPSBoostExtra=true"
        ]),
        "\n".join([
            "FFlagHighFPSBoost=true",
            "FFlagFrameRateUnlock=true",
            "FFlagVSyncOff=true",
            "FFlagRenderPriority=true",
            "FFlagFPSCapRemove=true",
            "FFlagDynamicFrameRate=true",
            "FFlagRenderThreadOptimize=true",
            "FFlagGPUFrameBuffer=2",
            "FFlagFrameQueueSize=3",
            "FFlagRenderBatchSize=28",
            "FFlagSyncRenderLoop=true",
            "FFlagFPSPriority=true",
            "FFlagHighFrameRateMode=true"
        ])
    ],
    "lowLatency": [
        "\n".join([
            "FFlagLowLatencyMode=true",
            "FFlagInputLagReduction=true",
            "FFlagFastResponse=true",
            "FFlagLatencySmoother=true",
            "FFlagQuickNet=true",
            "FFlagInputBufferSize=2",
            "FFlagNetResponseTime=50",
            "FFlagAsyncInputHandling=true",
            "FFlagLowLatencyPriority=true",
            "FFlagEventQueueOptimize=true",
            "FFlagInputPrediction=true",
            "FFlagLatencyCap=60"
        ]),
        "\n".join([
            "FFlagLowLatencyMode=true",
            "FFlagInputLagReduction=true",
            "FFlagFastResponse=true",
            "FFlagLatencySmoother=true",
            "FFlagQuickNet=true",
            "FFlagInputBufferSize=3",
            "FFlagNetResponseTime=40",
            "FFlagAsyncInputHandling=true",
            "FFlagLowLatencyPriority=true",
            "FFlagEventQueueOptimize=true",
            "FFlagInputPrediction=true",
            "FFlagLatencyCap=50",
            "FFlagLowLatencyBoost=true"
        ]),
        "\n".join([
            "FFlagLowLatencyMode=true",
            "FFlagInputLagReduction=true",
            "FFlagFastResponse=true",
            "FFlagLatencySmoother=true",
            "FFlagQuickNet=true",
            "FFlagInputBufferSize=1",
            "FFlagNetResponseTime=60",
            "FFlagAsyncInputHandling=true",
            "FFlagLowLatencyPriority=true",
            "FFlagEventQueueOptimize=true",
            "FFlagInputPrediction=true",
            "FFlagLatencyCap=70",
            "FFlagLowLatencyBoost=true",
            "FFlagInputSmoothing=true"
        ]),
        "\n".join([
            "FFlagLowLatencyMode=true",
            "FFlagInputLagReduction=true",
            "FFlagFastResponse=true",
            "FFlagLatencySmoother=true",
            "FFlagQuickNet=true",
            "FFlagInputBufferSize=4",
            "FFlagNetResponseTime=45",
            "FFlagAsyncInputHandling=true",
            "FFlagLowLatencyPriority=true",
            "FFlagEventQueueOptimize=true",
            "FFlagInputPrediction=true",
            "FFlagLatencyCap=55"
        ]),
        "\n".join([
            "FFlagLowLatencyMode=true",
            "FFlagInputLagReduction=true",
            "FFlagFastResponse=true",
            "FFlagLatencySmoother=true",
            "FFlagQuickNet=true",
            "FFlagInputBufferSize=2",
            "FFlagNetResponseTime=55",
            "FFlagAsyncInputHandling=true",
            "FFlagLowLatencyPriority=true",
            "FFlagEventQueueOptimize=true",
            "FFlagInputPrediction=true",
            "FFlagLatencyCap=65",
            "FFlagLowLatencyBoost=true"
        ])
    ],
    "textureOpt": [
        "\n".join([
            "FFlagTextureCompress=true",
            "FFlagLowResTextures=true",
            "FFlagTextureCache=true",
            "FFlagMipMapReduce=true",
            "FFlagTextureStream=true",
            "FFlagTextureQuality=1",
            "FFlagTextureMemoryLimit=256",
            "FFlagAsyncTextureLoad=true",
            "FFlagTextureDownscale=2",
            "FFlagTexturePriority=true",
            "FFlagTextureBatchSize=16",
            "FFlagTextureOptimization=true"
        ]),
        "\n".join([
            "FFlagTextureCompress=true",
            "FFlagLowResTextures=true",
            "FFlagTextureCache=true",
            "FFlagMipMapReduce=true",
            "FFlagTextureStream=true",
            "FFlagTextureQuality=2",
            "FFlagTextureMemoryLimit=512",
            "FFlagAsyncTextureLoad=true",
            "FFlagTextureDownscale=3",
            "FFlagTexturePriority=true",
            "FFlagTextureBatchSize=32",
            "FFlagTextureOptimization=true",
            "FFlagTextureCompressionLevel=2"
        ]),
        "\n".join([
            "FFlagTextureCompress=true",
            "FFlagLowResTextures=true",
            "FFlagTextureCache=true",
            "FFlagMipMapReduce=true",
            "FFlagTextureStream=true",
            "FFlagTextureQuality=1",
            "FFlagTextureMemoryLimit=128",
            "FFlagAsyncTextureLoad=true",
            "FFlagTextureDownscale=1",
            "FFlagTexturePriority=true",
            "FFlagTextureBatchSize=24",
            "FFlagTextureOptimization=true",
            "FFlagTextureCompressionLevel=1",
            "FFlagTextureStreamBoost=true"
        ]),
        "\n".join([
            "FFlagTextureCompress=true",
            "FFlagLowResTextures=true",
            "FFlagTextureCache=true",
            "FFlagMipMapReduce=true",
            "FFlagTextureStream=true",
            "FFlagTextureQuality=2",
            "FFlagTextureMemoryLimit=384",
            "FFlagAsyncTextureLoad=true",
            "FFlagTextureDownscale=2",
            "FFlagTexturePriority=true",
            "FFlagTextureBatchSize=20",
            "FFlagTextureOptimization=true",
            "FFlagTextureCompressionLevel=3"
        ]),
        "\n".join([
            "FFlagTextureCompress=true",
            "FFlagLowResTextures=true",
            "FFlagTextureCache=true",
            "FFlagMipMapReduce=true",
            "FFlagTextureStream=true",
            "FFlagTextureQuality=1",
            "FFlagTextureMemoryLimit=192",
            "FFlagAsyncTextureLoad=true",
            "FFlagTextureDownscale=3",
            "FFlagTexturePriority=true",
            "FFlagTextureBatchSize=28",
            "FFlagTextureOptimization=true"
        ])
    ],
    "graphicsRed": [
        "\n".join([
            "FFlagGraphicsMinimal=true",
            "FFlagShaderReduction=true",
            "FFlagLowDetail=true",
            "FFlagBasicRender=true",
            "FFlagLightOptimization=true",
            "FFlagShadowDisable=true",
            "FFlagParticleReduction=true",
            "FFlagRenderQuality=1",
            "FFlagPostProcessing=false",
            "FFlagAntiAliasing=false",
            "FFlagGraphicsMemoryLimit=512",
            "FFlagDrawDistance=500"
        ]),
        "\n".join([
            "FFlagGraphicsMinimal=true",
            "FFlagShaderReduction=true",
            "FFlagLowDetail=true",
            "FFlagBasicRender=true",
            "FFlagLightOptimization=true",
            "FFlagShadowDisable=true",
            "FFlagParticleReduction=true",
            "FFlagRenderQuality=2",
            "FFlagPostProcessing=false",
            "FFlagAntiAliasing=false",
            "FFlagGraphicsMemoryLimit=256",
            "FFlagDrawDistance=300",
            "FFlagGraphicsSimplify=true"
        ]),
        "\n".join([
            "FFlagGraphicsMinimal=true",
            "FFlagShaderReduction=true",
            "FFlagLowDetail=true",
            "FFlagBasicRender=true",
            "FFlagLightOptimization=true",
            "FFlagShadowDisable=true",
            "FFlagParticleReduction=true",
            "FFlagRenderQuality=1",
            "FFlagPostProcessing=false",
            "FFlagAntiAliasing=false",
            "FFlagGraphicsMemoryLimit=384",
            "FFlagDrawDistance=400",
            "FFlagGraphicsSimplify=true",
            "FFlagRenderBatchOptimize=true"
        ]),
        "\n".join([
            "FFlagGraphicsMinimal=true",
            "FFlagShaderReduction=true",
            "FFlagLowDetail=true",
            "FFlagBasicRender=true",
            "FFlagLightOptimization=true",
            "FFlagShadowDisable=true",
            "FFlagParticleReduction=true",
            "FFlagRenderQuality=1",
            "FFlagPostProcessing=false",
            "FFlagAntiAliasing=false",
            "FFlagGraphicsMemoryLimit=128",
            "FFlagDrawDistance=600",
            "FFlagGraphicsSimplify=true"
        ]),
        "\n".join([
            "FFlagGraphicsMinimal=true",
            "FFlagShaderReduction=true",
            "FFlagLowDetail=true",
            "FFlagBasicRender=true",
            "FFlagLightOptimization=true",
            "FFlagShadowDisable=true",
            "FFlagParticleReduction=true",
            "FFlagRenderQuality=2",
            "FFlagPostProcessing=false",
            "FFlagAntiAliasing=false",
            "FFlagGraphicsMemoryLimit=320",
            "FFlagDrawDistance=350",
            "FFlagGraphicsSimplify=true",
            "FFlagRenderBatchOptimize=true",
            "FFlagLowGraphicsMode=true"
        ])
    ],
    "flagForge": [
        "\n".join([
            "FlagForgeNetworkBoost=true",
            "FlagForgeGraphicsEnhance=false",
            "FlagForgeUIModernizeV2=true",
            "FlagForgePerfTrace=true",
            "FFlagNetworkOptimize=true",
            "FFlagRenderEnhance=false",
            "FFlagUIEnhance=true",
            "FFlagPerformanceTrace=true"
        ]),
        "\n".join([
            "FlagForgeNetworkBoost=false",
            "FlagForgeGraphicsEnhance=true",
            "FlagForgeUIModernizeV2=true",
            "FlagForgePerfTrace=true",
            "FFlagNetworkOptimize=false",
            "FFlagRenderEnhance=true",
            "FFlagUIEnhance=true",
            "FFlagPerformanceTrace=true",
            "FlagForgeBoostLevel=1"
        ]),
        "\n".join([
            "FlagForgeNetworkBoost=true",
            "FlagForgeGraphicsEnhance=false",
            "FlagForgeUIModernizeV2=false",
            "FlagForgePerfTrace=true",
            "FFlagNetworkOptimize=true",
            "FFlagRenderEnhance=false",
            "FFlagUIEnhance=false",
            "FFlagPerformanceTrace=true"
        ]),
        "\n".join([
            "FlagForgeNetworkBoost=true",
            "FlagForgeGraphicsEnhance=true",
            "FlagForgeUIModernizeV2=true",
            "FlagForgePerfTrace=false",
            "FFlagNetworkOptimize=true",
            "FFlagRenderEnhance=true",
            "FFlagUIEnhance=true",
            "FFlagPerformanceTrace=false",
            "FlagForgeBoostLevel=2"
        ]),
        "\n".join([
            "FlagForgeNetworkBoost=false",
            "FlagForgeGraphicsEnhance=false",
            "FlagForgeUIModernizeV2=true",
            "FlagForgePerfTrace=true",
            "FFlagNetworkOptimize=false",
            "FFlagRenderEnhance=false",
            "FFlagUIEnhance=true",
            "FFlagPerformanceTrace=true"
        ])
    ]
}

# Custom CSS to style the app (similar to the original design)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #134e4a, #5eead4);
    padding: 20px;
}
.container {
    background: white;
    border-radius: 16px;
    padding: 32px;
    max-width: 600px;
    width: 100%;
    margin: auto;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    border: 1px solid #d1d5db;
}
h1 {
    text-align: center;
    color: #134e4a;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 24px;
}
.stButton>button {
    background: #22c55e;
    color: white;
    border: none;
    padding: 14px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
    width: 100%;
    margin: 12px 0;
}
.stButton>button:hover {
    background: #16a34a;
    box-shadow: 0 0 10px rgba(34, 197, 94, 0.5);
}
.preset-button {
    background: #4b5563;
    color: white;
    border: none;
    padding: 12px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    margin: 6px;
}
.preset-button:hover {
    background: #134e4a;
    box-shadow: 0 0 10px rgba(94, 234, 212, 0.5);
}
.output-box {
    background: #f9fafb;
    padding: 16px;
    border-radius: 8px;
    min-height: 120px;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    color: #1f2937;
    white-space: pre-wrap;
    overflow-x: auto;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    max-height: 200px;
    overflow-y: auto;
}
.footer {
    color: #f3f4f6;
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
}
@media (max-width: 600px) {
    .container {
        padding: 16px;
    }
    h1 {
        font-size: 24px;
    }
    .stButton>button, .preset-button {
        font-size: 14px;
        padding: 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown("<h1>Roblox FFlag Generator</h1>", unsafe_allow_html=True)

# Options (checkboxes)
st.markdown("### Options", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    low_ping = st.checkbox("Low Ping")
    high_fps = st.checkbox("High FPS")
    low_latency = st.checkbox("Low Latency")
with col2:
    texture_opt = st.checkbox("Texture Optimization")
    graphics_red = st.checkbox("Graphics Reduction")
    flag_forge = st.checkbox("FlagForge Enhancements")

# Presets
st.markdown("### Presets", unsafe_allow_html=True)
col3, col4, col5, col6 = st.columns(4)
with col3:
    if st.button("Max Performance", key="max"):
        low_ping, high_fps, low_latency, texture_opt, graphics_red, flag_forge = False, True, False, True, True, False
        st.session_state["low_ping"] = low_ping
        st.session_state["high_fps"] = high_fps
        st.session_state["low_latency"] = low_latency
        st.session_state["texture_opt"] = texture_opt
        st.session_state["graphics_red"] = graphics_red
        st.session_state["flag_forge"] = flag_forge
with col4:
    if st.button("Low-End Device", key="low"):
        low_ping, high_fps, low_latency, texture_opt, graphics_red, flag_forge = False, False, False, True, True, False
        st.session_state["low_ping"] = low_ping
        st.session_state["high_fps"] = high_fps
        st.session_state["low_latency"] = low_latency
        st.session_state["texture_opt"] = texture_opt
        st.session_state["graphics_red"] = graphics_red
        st.session_state["flag_forge"] = flag_forge
with col5:
    if st.button("Balanced Mode", key="balanced"):
        low_ping, high_fps, low_latency, texture_opt, graphics_red, flag_forge = True, True, True, False, False, False
        st.session_state["low_ping"] = low_ping
        st.session_state["high_fps"] = high_fps
        st.session_state["low_latency"] = low_latency
        st.session_state["texture_opt"] = texture_opt
        st.session_state["graphics_red"] = graphics_red
        st.session_state["flag_forge"] = flag_forge
with col6:
    if st.button("FlagForge Mode", key="flagforge"):
        low_ping, high_fps, low_latency, texture_opt, graphics_red, flag_forge = True, True, False, False, False, True
        st.session_state["low_ping"] = low_ping
        st.session_state["high_fps"] = high_fps
        st.session_state["low_latency"] = low_latency
        st.session_state["texture_opt"] = texture_opt
        st.session_state["graphics_red"] = graphics_red
        st.session_state["flag_forge"] = flag_forge

# Update checkbox states from session state (if preset was clicked)
low_ping = st.session_state.get("low_ping", low_ping)
high_fps = st.session_state.get("high_fps", high_fps)
low_latency = st.session_state.get("low_latency", low_latency)
texture_opt = st.session_state.get("texture_opt", texture_opt)
graphics_red = st.session_state.get("graphics_red", graphics_red)
flag_forge = st.session_state.get("flag_forge", flag_forge)

# Generate FFlags button
if "output" not in st.session_state:
    st.session_state["output"] = ""

if st.button("Generate FFlags"):
    preferences = []
    if low_ping:
        preferences.append("lowPing")
    if high_fps:
        preferences.append("highFPS")
    if low_latency:
        preferences.append("lowLatency")
    if texture_opt:
        preferences.append("textureOpt")
    if graphics_red:
        preferences.append("graphicsRed")
    if flag_forge:
        preferences.append("flagForge")

    output = ""
    for pref in preferences:
        flags = fflag_library[pref]
        random_flag_set = random.choice(flags)
        output += random_flag_set + "\n\n"

    st.session_state["output"] = output.strip() if output else "Please select at least one preference."

# Display output
st.markdown(f'<div class="output-box">{st.session_state["output"]}</div>', unsafe_allow_html=True)

# Copy to Clipboard button
if st.button("Copy to Clipboard"):
    if st.session_state["output"] and st.session_state["output"] != "Please select at least one preference.":
        st.write('<script>navigator.clipboard.writeText("' + st.session_state["output"] + '").then(() => alert("FFlags copied to clipboard!"));</script>', unsafe_allow_html=True)
    else:
        st.error("Nothing to copy! Generate FFlags first.")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Kelsier</div>', unsafe_allow_html=True)
