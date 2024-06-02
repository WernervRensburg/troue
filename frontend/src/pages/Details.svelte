<script>
  import CustomFlipClock from "../lib/components/FlipClock.svelte";
  import RsvpComponent from "../lib/components/RSVPComponent.svelte";

  import { onMount } from "svelte";

  import venueImages from "../assets/images/venue-images.png";

  const targetDate = new Date("2024-10-26T16:00:00");

  let myCustomDate = new Date();

  function updateCountdown() {
    const now = new Date();
    const timeRemaining = targetDate.getTime() - now.getTime();

    if (timeRemaining > 0) {
      const totalDays = Math.ceil(timeRemaining / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

      myCustomDate.setFullYear(2024);
      myCustomDate.setMonth(0);
      myCustomDate.setDate(totalDays);
      myCustomDate.setHours(hours);
      myCustomDate.setMinutes(minutes);
      myCustomDate.setSeconds(seconds);
    } else {
      myCustomDate.setHours(0);
      myCustomDate.setMinutes(0);
      myCustomDate.setSeconds(0);
    }
  }

  let interval;
  onMount(() => {
    interval = setInterval(updateCountdown, 1000);
    return () => {
      clearInterval(interval);
    };
  });
</script>

<div class="main-wrapper">
  <div class="main-details-wrapper">
    <span class="main-header">Die Details</span>
    <div class="vd-wrapper">
      <div class="vd-left"></div>
      <div class="vd-right"></div>
    </div>
    <div class="when-icon">
      <i class="fa-regular fa-clock d-icon fa-2xl"></i>
    </div>
    <div class="when">26 Oktober 2024, 04:00 PM</div>
    <div class="countdown">
      <CustomFlipClock
        bind:date={myCustomDate}
        showMonths={true}
        showDays={true}
        showHours={true}
        showMinutes={true}
        showSeconds={true}
        size={1}
      />
    </div>
    <span class="main-header venue-header">Die Venue</span>
    <div class="vd-wrapper">
      <div class="vd-left"></div>
      <div class="vd-right"></div>
    </div>
    <div class="where-icon">
      <i class="fa-solid fa-location-dot fa-2xl d-icon"></i>
    </div>
    <div class="where">
      Louvain Guest Farm, Herold
    </div>
    <div class="directions">
      <iframe
        class="directions-i"
        title="Directions"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3315.0517387712734!2d22.645873976490577!3d-33.81097787324878!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1e78aa5c9f79c6bf%3A0xf312fd42c844633d!2sLouvain%20Guest%20Farm!5e0!3m2!1sen!2sza!4v1716314598236!5m2!1sen!2sza"
        width="600"
        height="450"
        style="border:0;"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>
    <div class="vd-wrapper">
      <div class="vd-left"></div>
      <div class="vd-right"></div>
    </div>
    <img class="venue-images" src={venueImages} alt="images of the venue" />
  </div>
  <div class="other-details-wrapper">
    <div class="accomodation">
      <span class="main-header venue-header">Akkommodasie</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <p class="acc-p">
        Die indeling van gaste in die glamping en stalle word deur ons <strong>alleenlik</strong> gedoen nadat die RSVPs
        gefinaliseer is - Dui aan in die RSVP hoeveel aande oorgebly gaan word
          .<br /><br />

        Daar is 2 tipes akkommodasie beskikbaar op die venue, glamping of die stalle.<br /><br />

        Die stalle vat 3 persone per stal en die glamping vat 2 persone per tent.<br /><br />

        Die kostes vir die stalle is R450pppn indien albei aande gebly word, andersins is dit
        R700pp vir 1 aand.<br /><br />

        Die kostes vir die glamping is R350pppn indien albei aande gebly word, andersins is
        dit R1000 per tent (R500pp).<br /><br />

        Die betaling van die verblyf word deur Louvain hanteer, Louvain stuur self n faktuur
        uit na die gaste wat oorbly nadat ons almal ingedeel het.<br /><br />
      </p>
    </div>
    <div class="friday-event">
      <span class="main-header venue-header">Vrydagaand</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <p class="fri-p">
        Ons gaan die Vrydagaand 'n lekker kuier vuur maak by die glamping area.<br /><br />
        Daar sal platters voorsien word, terwyl drank en enige ander kosse die
        gaste se eie verantwoordelikheid is.<br /><br />
        Tyd is vanaf 05:00PM
      </p>
    </div>
    <div class="dresscode">
      <span class="main-header venue-header">Saterdag</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <p class="dress-p">
        Ontbyt is gaste se eie verantwoordelikheid. Daar is 'n opsie om ontbyt te koop vir R95.
      </p>
    </div>
    <div class="dresscode">
      <span class="main-header venue-header">Seremonie</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <p class="dress-p">
        Die seremonie begin Saterdag 4 uur by die ou klip kerk.
      </p>
    </div>
    <div class="dresscode">
      <span class="main-header venue-header">Kleredrag</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <p class="dress-p">
        - Cocktail drag -
      </p>
    </div>
    <div class="rsvp">
      <span class="main-header venue-header">RSVP</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <RsvpComponent />
    </div>
    <div class="registry">
      <span class="main-header venue-header">Register</span>
      <div class="vd-wrapper">
        <div class="vd-left"></div>
        <div class="vd-right"></div>
      </div>
      <p class="reg-p">
        Daar sal 'n houer op die dag beskikbaar wees waarin koeverte geplaas kan word.
      </p>
    </div>
  </div>
</div>

<style>
  .main-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .main-wrapper div {
    box-sizing: border-box;
    max-width: 1000px;
    width: 100%;
    padding: 15px;
  }

  .main-details-wrapper {
    background-color: azure;
    display: flex;
    flex-direction: column;
  }

  .vd-wrapper {
    display: flex;
  }

  .vd-right,
  .vd-left {
    height: 55px;
    user-select: none;
  }

  .vd-right {
    border-left: 1px solid #ad925d !important;
  }

  .vd-left {
    border-right: 1px solid #ad925d !important;
  }

  .d-icon {
    color: #ad925d !important;
  }

  .main-header {
    font-size: 32px;
  }

  .where,
  .when {
    font-size: 20px;
  }

  .main-header,
  .where,
  .when {
    font-family: "QueenSides";
    color: #ad925d;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    user-select: none;
  }

  .countdown {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  .directions-i {
    max-width: 100%;
  }

  .venue-images {
    max-width: 100%;
    padding-top: 25px;
  }

  .venue-header {
    padding-top: 30px;
  }

  .acc-p,
  .reg-p,
  .fri-p,
  .dress-p {
    font-family: "QueenSides";
    font-size: 20px;
    color: #ad925d;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    user-select: none;
  }

  @media (min-width: 1000px) {
    .acc-p,
    .reg-p,
    .fri-p,
    .dress-p,
    .where,
    .when {
      font-size: 24px;
    }
    .main-header {
      font-size: 36px;
    }
  }

  .other-details-wrapper {
    background-color: #e6fcfc;
  }
</style>
