init 10 python:
    WNFH_SHADER_NAME = "wnfh.DynamicShader"

    WNFH_DS_VARIABLES = """
        uniform float u_time;
        uniform float u_lod_bias;
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_dissolvePower;
        uniform float u_smoothPower;
        uniform float u_outlinesPower;
        uniform float u_internalTransparencyPower;
        uniform vec2 u_scroll1;
        uniform vec2 u_scroll2;
        uniform vec2 u_scroll3;

        attribute vec2 a_tex_coord;

        varying vec2 v_tex_coord;
    """

    WNFH_DS_VERTEX_300 = """
        v_tex_coord = a_tex_coord;
    """

    WNFH_DS_FRAGMENT_300 = """       
        vec4 child = texture2D(tex0, v_tex_coord, u_lod_bias);
        float noiseAlpha1 = texture2D(tex1, v_tex_coord + u_scroll1 * u_time, u_lod_bias).r;
        float noiseAlpha2 = texture2D(tex1, v_tex_coord + u_scroll2 * u_time, u_lod_bias).r;
        float noiseAlpha3 = texture2D(tex1, v_tex_coord + u_scroll3 * u_time, u_lod_bias).r;
        float mixedNoiseAlpha = noiseAlpha1 * noiseAlpha2 * noiseAlpha3 * u_dissolvePower;
        
        mixedNoiseAlpha = smoothstep(u_smoothPower, 1.0, mixedNoiseAlpha);

        float pixelBrightness = clamp(mixedNoiseAlpha * child.a, 0.0, 1.0);

        gl_FragColor = vec4(child.rgb * pixelBrightness, pixelBrightness);

        gl_FragColor += step(0.0125, gl_FragColor.a) * gl_FragColor.a * ((1.0 - gl_FragColor.a) * u_outlinesPower - u_internalTransparencyPower);
    """

    renpy.register_shader(WNFH_SHADER_NAME, variables=WNFH_DS_VARIABLES, vertex_300=WNFH_DS_VERTEX_300, fragment_300=WNFH_DS_FRAGMENT_300)



