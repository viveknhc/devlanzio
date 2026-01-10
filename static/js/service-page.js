gsap.registerPlugin(ScrollTrigger);

const servicePanels = gsap.utils.toArray(".service-panel");
servicePanels.pop(); // remove last panel (same as original logic)

servicePanels.forEach((panel) => {
    const tl = gsap.timeline({
        scrollTrigger: {
            trigger: panel,
            start: "bottom bottom",
            pin: true,
            pinSpacing: false,
            scrub: true,
            onRefresh: () => {
                gsap.set(panel, {
                    transformOrigin: "center " +
                        (panel.offsetHeight - window.innerHeight / 2) +
                        "px",
                });
            },
        },
    });

    tl.fromTo(
        panel, {
            y: 0,
            rotate: 0,
            scale: 1,
            opacity: 1,
        }, {
            y: 0,
            rotateX: 0,
            scale: 0.5,
            opacity: 0.5,
        },
        0
    ).to(panel, {
        opacity: 0,
        duration: 0.1
    });
});