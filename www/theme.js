const getWidgets = () => {
  const view = document
    .querySelector("home-assistant")
    .shadowRoot.querySelector("home-assistant-main")
    .shadowRoot.querySelector("app-drawer-layout")
    .querySelector("ha-panel-lovelace")
    .shadowRoot.querySelector("hui-root")
    .shadowRoot.querySelector("ha-app-layout")
    .querySelector("hui-view").shadowRoot;

  return view.querySelectorAll(".column > *");
};

const labelToColour = label =>
  ({
    red: "#cc241e",
    green: "#689d6a",
    blue: "#458587",
    purple: "#b16286",
    sky: "#83a598",
    sun: "#fabe30",
    white: "rgb(255, 100, 109)",
    mint: "rgb(146, 159, 127)",
  }[label.toLowerCase()]);

const applyStyle = (el, css) => {
  const style = document.createElement("style");
  style.textContent = css;
  el.appendChild(style);
};

const applyIconColours = () => {
  const horizontalStacks = Array.from(getWidgets()).filter(
    each => each._config.type === "horizontal-stack"
  );

  horizontalStacks.forEach(each => {
    // Get all the labels from the config
    const labels = each._config.cards.map(card =>
      (card.name || "").toLowerCase()
    );

    // Filter to entity-button cards within stack
    const entityButtonCards = each.shadowRoot.querySelectorAll(
      "hui-entity-button-card"
    );

    // Select the exact ha-card within each entity-button-card (paired against it's label)
    const cards = Array.from(entityButtonCards)
      .map((card, i) => ({
        el: card.shadowRoot.querySelector("ha-card"),
        label: labels[i]
      }))
      .filter(each => !!each.el);

    for (let i = 0; i < cards.length; i++) {
      const { el, label } = cards[i];
      const iconColour = labelToColour(label);
      if (iconColour) {
        applyStyle(
          el,
          ` span { font-size2:0.8em; color: #999; } ha-icon { fill: ${iconColour} `
        );
      }
    }
  });
};

window.onload = () => {
  console.log("on load");
  applyIconColours();
};

window.onresize = () => {
  console.log("on resize");
  applyIconColours();
};
