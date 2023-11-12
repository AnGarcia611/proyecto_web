def figure(profile,bolt, n_bolts,fit):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    from placa_base.geometry import Profile, Bolt, BPlate
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    perfil = Profile(profile)
    shape = perfil.profile_shape()
    x=[]
    y=[]
    for point in shape:
        x.append(point[0])
        y.append(point[1])

    ax.fill(x,y, "red")


    pernos = Bolt(bolt)
    pernos_shape = pernos.bolts_shape(perfil,fit=fit,number=n_bolts)

    for point in pernos_shape:
        circle = Circle(point, pernos.bolt_diameter/2, color='red')
        ax.add_patch(circle)

    placa = BPlate()
    bp_shape = placa.bp_shape(profile=perfil,bolt=pernos,fit=fit)
    x=[]
    y=[]
    for point in bp_shape:
        x.append(point[0])
        y.append(point[1])

    plt.plot(x, y, fillstyle='none')

    ax.set_aspect(1)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    
    return fig