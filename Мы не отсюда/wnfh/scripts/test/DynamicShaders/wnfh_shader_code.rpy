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

#### Raindrops #####

    #<Шейдеры взяты с Shadertoy.>#
    #<Ссылка: https://www.shadertoy.com/view/slfSzS>#
    #<Не используйте в коммерческих проектах.>#
    ##<Я ЛИШЬ ПЕРЕНЁС ШЕЙДЕР НА RenPy.>##

    SRD_SHADER_NAME = "SRD.ScreenRainDrops"

    SRD_VARIABLES = """
        uniform float u_lod_bias;
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_time;
        uniform float u_general_size;
        uniform float u_puddles_size;
        uniform float u_trail_color_shift;
        uniform float u_drop_speed;
        uniform float u_rain_distance;
        uniform float u_blur_size;

        attribute vec2 a_tex_coord;

        varying vec2 v_tex_coord;
    """

    SRD_VERTEX_300 = """
        v_tex_coord = a_tex_coord;
    """

    SRD_FRAGMENT_300 = """
        trailColorShift = u_trail_color_shift;
        generalSize = u_general_size;
        puddlesSize = u_puddles_size;

        float child_alpha = texture2D(tex0, v_tex_coord, u_lod_bias).a;

        vec2 uv = -u_rain_distance * v_tex_coord.xy;
        vec2 UV = v_tex_coord;
        
        float t = u_time * u_drop_speed;      
        
        UV = (UV-.5)*(.9)+.5;
        
        vec2 c = Rain(uv, t);

        vec2 e = vec2(.001, 0.0);
        float cx = Rain(uv+e, t).x;
        float cy = Rain(uv+e.yx, t).x;
        vec2 n = vec2(cx-c.x, cy-c.x);

        // BLUR
        float Pi2 = 6.28318530718; // Pi*2
    
        float Directions = 32.0; // BLUR DIRECTIONS
        float Quality = 8.0; // BLUR QUALITY

        vec2 Radius = u_blur_size / res0.xy;

        vec3 col = texture2D(tex0, UV).rgb;
        // Blur calculations
        for(float d = 0.0; d < Pi2; d += Pi2/Directions)
        {
            for(float i= 1.0 / Quality; i <= 1.0; i += 1.0/Quality)
            {
                vec3 tex = texture2D(tex0, UV+n+vec2(cos(d),sin(d))*Radius*i).rgb;
                col += tex;            
            }
        }

        col /= Quality * Directions - 0.0;
        // END BLUR

        vec3 tex = texture2D(tex0, UV+n).rgb;
        c.y = clamp(c.y, 0.0, 1.);

        col -= c.y;
        col += c.y*(tex+.6);
        
        gl_FragColor = vec4(col, child_alpha);
    """
    SRD_SHADER_FUNCTIONS = """
        float trailColorShift = 0.0;
        float generalSize = 0.0;
        float puddlesSize = 0.0;

        vec3 N13(float p) {
            vec3 p3 = fract(vec3(p) * vec3(.1031,.11369,.13787));
            p3 += dot(p3, p3.yzx + 19.19);
            return fract(vec3((p3.x + p3.y)*p3.z, (p3.x+p3.z)*p3.y, (p3.y+p3.z)*p3.x));
        }

        vec4 N14(float t) {
            return fract(sin(t*vec4(123., 1024., 1456., 264.))*vec4(6547., 345., 8799., 1564.));
        }
        float N(float t) {
            return fract(sin(t*12345.564)*7658.76);
        }

        float Saw(float b, float t) {
            return smoothstep(0., b, t)*smoothstep(1., b, t);
        }

        vec2 Drops(vec2 uv, float t) {
            vec2 UV = uv;
            
            uv.y += t*0.8;
            vec2 a = vec2(puddlesSize, 1.);
            vec2 grid = a*2.;
            vec2 id = floor(uv*grid);
            
            float colShift = N(id.x); 
            uv.y += colShift;
            
            id = floor(uv*grid);
            vec3 n = N13(id.x*35.2+id.y*2376.1);
            vec2 st = fract(uv*grid)-vec2(.5, 0);
            
            float x = n.x-.5;
            
            float y = UV.y*20.;
            
            float distort = sin(y+sin(y));
            x += distort*(0.5-abs(x))*(n.z-0.5);
            x *= 0.7;
            float ti = fract(t+n.z);
            y = (Saw(0.85, ti)-0.5)*0.9+.5;
            vec2 p = vec2(x, y);
            
            float d = length((st-p)*a.yx);
            
            float dSize = generalSize; 
            
            float Drop = smoothstep(dSize, 0.0, d);
            
            float r = sqrt(smoothstep(1., y, st.y));
            float cd = abs(st.x-x);
            
            float trail = smoothstep((dSize*.5+.03)*r, (dSize*0.5-0.05)*r, cd);
            float trailFront = smoothstep(-0.02, 0.02, st.y-y);
            trail *= trailFront * trailColorShift;
            
            y = UV.y;
            y += N(id.x);
            float trail2 = smoothstep(dSize*r, .0, cd);
            float droplets = max(0., (sin(y*(1.-y)*120.)-st.y))*trail2*trailFront*n.z;
            y = fract(y*10.)+(st.y-.5);
            float dd = length(st-vec2(x, y));
            droplets = smoothstep(dSize*N(id.x), 0., dd);
            float m = Drop + droplets * r * trailFront;
            
            
            return vec2(m, trail);
        }

        float StaticDrops(vec2 uv, float t) {
            uv *= 30.;
            
            vec2 id = floor(uv);
            uv = fract(uv)-.5;
            vec3 n = N13(id.x*107.45+id.y*3543.654);
            vec2 p = (n.xy-.5)*0.5;
            float d = length(uv-p);
            
            float fade = Saw(.025, fract(t+n.z));
            float c = smoothstep(generalSize, 0., d)*fract(n.z*10.)*fade;

            return c;
        }

        vec2 Rain(vec2 uv, float t) {
            float s = StaticDrops(uv, t); 
            vec2 r1 = Drops(uv, t);
            vec2 r2 = Drops(uv*1.8, t);
            
            float c = s+r1.x+r2.x;
            
            c = smoothstep(.3, 1., c);
            
            return vec2(c, max(r1.y, r2.y));
        }
    """

    renpy.register_shader(SRD_SHADER_NAME, variables=SRD_VARIABLES, vertex_300=SRD_VERTEX_300, fragment_300=SRD_FRAGMENT_300, fragment_functions=SRD_SHADER_FUNCTIONS)
