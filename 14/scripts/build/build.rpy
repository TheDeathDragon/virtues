define gui.display_version = '14'
define config.version = 1400
define gui.version_suffix = ''
define build.directory_name = 'VIRTUES-v14'




define build_platform = "pc"
define asset_type = "pc"
define partial_build = False


define gui.main_menu_background = "bg14"
define gui.splash_art = "splash14"


init python:
    BUILD_TYPES = ('android', 'pc', 'low', 'lossless')
    assert(build_type in ("pc", "android"))
    assert(asset_type in BUILD_TYPES)
    discard_types = [x for x in BUILD_TYPES if x != asset_type]

    archive_type = "android" if build_platform == "android" else "renpy"

    build.executable_name = 'VIRTUES'


    build.archive('scripts', 'all')
    build.archive('gui', 'all')
    build.archive('audio', 'all')
    build.archive('music', 'all')
    build.archive('sfx', 'all')
    build.archive('general_images', 'all')
    build.archive('thumbnails', 'all')




    build.archive('patch05a', archive_type)
    build.archive('patch06', archive_type)
    build.archive('patch07', archive_type)
    build.archive('patch10a', archive_type)
    build.archive('patch1310', archive_type)

    build.archive('cg05', archive_type)
    build.archive('cg05a', archive_type)
    build.archive('cg06', archive_type)
    build.archive('cg06b', archive_type)
    build.archive('cg07', archive_type)
    build.archive('cg08', archive_type)
    build.archive('cg09', archive_type)
    build.archive('cg10', archive_type)
    build.archive('cg11', archive_type)
    build.archive('cg12', archive_type)
    build.archive('cg13', archive_type)
    build.archive('cg1310', archive_type)
    build.archive('cg14', archive_type)

    build.archive('videos05', archive_type)
    build.archive('videos06', archive_type)
    build.archive('videos07', archive_type)
    build.archive('videos08', archive_type)
    build.archive('videos09', archive_type)
    build.archive('videos10', archive_type)
    build.archive('videos10b', archive_type)
    build.archive('videos11', archive_type)
    build.archive('videos12', archive_type)
    build.archive('videos13', archive_type)
    build.archive('videos1310', archive_type)
    build.archive('videos14', archive_type)

    if partial_build:
        build.classify('game/fonts/**', None)
        build.classify('game/images/thumbnails/**', None)
        build.classify('game/gui/**', None)
        build.classify('game/music/**', None)
        build.classify('game/sfx/**', None)
        build.classify('game/audio/**', None)
        
        build.classify('game/images/general/**', None)
        build.classify('game/images/cg*/**', None)
        build.classify('game/images/vfframe*/**', None)
        
        build.classify('game/videos/**', None)
        build.classify('game/videos/05_lossless/**', None)
        build.classify('game/videos/06_lossless/**', None)
        build.classify('game/videos/07_lossless/**', None)
        build.classify('game/videos/08_lossless/**', None)
        build.classify('game/videos/09_lossless/**', None)
        build.classify('game/videos/10_lossless/**', None)
        build.classify('game/videos/10b_lossless/**', None)
        build.classify('game/videos/11_lossless/**', None)
        build.classify('game/videos/12_lossless/**', None)
        build.classify('game/videos/13_lossless/**', None)
        build.classify('game/videos/1310_lossless/**', None)
        
        build.classify('game/patches/**', None)



    build.classify('game/images/cg05_{}/**'.format(asset_type), 'cg05')
    build.classify('game/images/cg05a_{}/**'.format(asset_type), 'cg05a')
    build.classify('game/images/cg06_{}/**'.format(asset_type), 'cg06')
    build.classify('game/images/cg06b_{}/**'.format(asset_type), 'cg06b')
    build.classify('game/images/cg07_{}/**'.format(asset_type), 'cg07')
    build.classify('game/images/cg08_{}/**'.format(asset_type), 'cg08')
    build.classify('game/images/cg09_{}/**'.format(asset_type), 'cg09')
    build.classify('game/images/cg10_{}/**'.format(asset_type), 'cg10')
    build.classify('game/images/cg11_{}/**'.format(asset_type), 'cg11')
    build.classify('game/images/cg12_{}/**'.format(asset_type), 'cg12')
    build.classify('game/images/cg13_{}/**'.format(asset_type), 'cg13')
    build.classify('game/images/cg1310_{}/**'.format(asset_type), 'cg1310')
    build.classify('game/images/cg14_{}/**'.format(asset_type), 'cg14')


    build.classify('game/videos/05_lossless/**', 'videos05')
    build.classify('game/videos/06_lossless/**', 'videos06')
    build.classify('game/videos/07_lossless/**', 'videos07')
    build.classify('game/videos/08_lossless/**', 'videos08')
    build.classify('game/videos/09_lossless/**', 'videos09')
    build.classify('game/videos/10_lossless/**', 'videos10')
    build.classify('game/videos/10b_lossless/**', 'videos10b')
    build.classify('game/videos/11_lossless/**', 'videos11')
    build.classify('game/videos/12_lossless/**', 'videos12')
    build.classify('game/videos/13_lossless/**', 'videos13')
    build.classify('game/videos/1310_lossless/**', 'videos1310')
    build.classify('game/videos/14_lossless/**', 'videos14')


    build.classify('game/images/vfframe05_{}/**'.format(asset_type), 'videos05')
    build.classify('game/images/vfframe06_{}/**'.format(asset_type), 'videos06')
    build.classify('game/images/vfframe07_{}/**'.format(asset_type), 'videos07')
    build.classify('game/images/vfframe08_{}/**'.format(asset_type), 'videos08')
    build.classify('game/images/vfframe09_{}/**'.format(asset_type), 'videos09')
    build.classify('game/images/vfframe10_{}/**'.format(asset_type), 'videos10')
    build.classify('game/images/vfframe11_{}/**'.format(asset_type), 'videos11')
    build.classify('game/images/vfframe12_{}/**'.format(asset_type), 'videos12')
    build.classify('game/images/vfframe13_{}/**'.format(asset_type), 'videos13')
    build.classify('game/images/vfframe1310_{}/**'.format(asset_type), 'videos1310')
    build.classify('game/images/vfframe14_{}/**'.format(asset_type), 'videos14')



    build.classify('game/patches/05a_{}/**'.format(asset_type), 'patch05a')
    build.classify('game/patches/06_{}/**'.format(asset_type), 'patch06')
    build.classify('game/patches/07_{}/**'.format(asset_type), 'patch07')
    build.classify('game/patches/10a_{}/**'.format(asset_type), 'patch10a')
    build.classify('game/patches/10b_{}/**'.format(asset_type), 'patch10b')
    build.classify('game/patches/1310_{}/**'.format(asset_type), 'patch1310')

    for dtype in discard_types:
        build.classify('game/images/*_{}/**'.format(dtype), None)
        
        build.classify('game/patches/*_{}/**'.format(dtype), None)





    build.classify('game/images/general/**', 'general_images')

    build.classify('game/images/thumbnails/**', 'thumbnails')

    build.classify('game/gui/**', 'gui')

    build.classify('game/music/**', 'music')

    build.classify('game/sfx/**', 'sfx')

    build.classify('game/audio/**', 'audio')

    build.classify('**.py', 'scripts')
    build.classify('**.rpyc', 'scripts')
    build.classify('**.pem', 'scripts')
    build.classify('**.json', 'scripts')      




    build.classify('**.rpy', None)
    build.classify('**.txt', None)  
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('**.ai', None)
    build.classify('**.zip', None)
    build.classify('.**', None)
    build.classify('**.log', None)
    build.classify('**.code-workspace', None)
    build.classify('hooks', None)
    build.classify('lfs', None)
    build.classify('*.py', None)
    build.classify('tools/**', None)
    build.classify('build_tool/**', None)
    build.classify('__pycache__/**', None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
