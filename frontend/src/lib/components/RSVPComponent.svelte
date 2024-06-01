<script>
  let rsvpStage = 0;
  let postData = {};
  let responseData = null;

  let foundGuest = false;
  $: guestData = [];

  let name = "";

  $: findGuestData = {
    name: name,
  };

  let email = "";
  let emailValid = false;

  let options = [
    { value: "vrydagaand", text: "Slegs Vrydagaand" },
    { value: "saterdagaand", text: "Slegs Saterdagaand" },
    { value: "albei", text: "Albei aande" },
    { value: "geen", text: "Gaan nie oorbly nie" },
  ];

  let anyAttendance = false;

  async function findInvite() {
    rsvpStage += 1;

    try {
      const response = await fetch("http://127.0.0.1:5000/guests/find_guest?format=json", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(findGuestData),
      });

      const responseStatus = response.status;

      if (responseStatus === 200) {
        responseData = await response.json();
        console.log(responseData);
        guestData = responseData;
        foundGuest = true;
      }
    } catch (error) {
      console.log(error);
    }
  }

  async function saveGuestResponse() {
    rsvpStage += 1;

    try {
      const response = await fetch("http://127.0.0.1:5000/guests/save_response?format=json", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(guestData),
      });

      const responseStatus = response.status;

      if (responseStatus === 200) {
        responseData = await response.json();
        console.log(responseData);
        guestData = responseData;
        foundGuest = true;
      }
    } catch (error) {
      console.log(error);
    }
  }

  function increaseRsvpStage() {
    
    if (rsvpStage === 2 && !anyAttendance) rsvpStage = -1;
    else rsvpStage += 1;
  }

  function decreaseRsvpStage() {
    rsvpStage -= 1;
  }

  function resetRSVP() {
    guestData = [];
    responseData = [];
    rsvpStage -= 1;
  }

  function handleEmailChange() {
    emailValid = /\S+@\S+\.\S+/.test(email);
    if (!emailValid) return;
    guestData = guestData.map(guest => ({ ...guest, email }));
  }

  function handleGuestAttendance(guestID, response) {
    guestData = guestData.map((guest) => {
      if (guest.id === guestID) {
        return { ...guest, attendance: response };
      }
      return guest;
    });
    guestData = [...guestData];
    console.log(guestData);

    anyAttendance = guestData.some(guest => guest.attendance);
  }

  function handleGuestAccomodation(guestID, event) {
    const selectedValue = event.target.value;

    guestData = guestData.map((guest) => {
      if (guest.id === guestID) {
        return { ...guest, accommodation: selectedValue };
      }
      return guest;
    });
    guestData = [...guestData];
    console.log(guestData);
  }
</script>

<div class="rsvp-wrapper">
  {#if rsvpStage === 0}
    <div class="find-inv-wrapper">
      <p class="rsvp-desc">
        Indien jy vir jou en 'n gas RSVP
        (of jou familie)
        sal jy kan RSVP vir die hele groep.
      </p>
      <div class="form">
        <input class="fn-input" placeholder="Volle Naam en Van" bind:value={name} />
        <button class="find-invite-btn" on:click={findInvite}>Vind Jou Uitnodiging</button>
      </div>
    </div>
  {:else if rsvpStage === 1}
    <div class="found-inv-wrapper">
      {#if foundGuest}
        <span class="general-text">Die volgende uitnodigings is gevind</span>
        {#each guestData as guest}
          <div class="guest-wrapper">
            <span class="guest-name">{guest.fullname}</span>
          </div>
        {/each}
        <button class="find-invite-btn" on:click={increaseRsvpStage}>Volgende</button>
      {:else}
        <span class="general-text">Daar is ongelukkig nie n uitnodiging aan daardie naam gekoppel nie.</span>
      {/if}
      <button class="find-invite-btn" on:click={resetRSVP}>Soek Weer</button>
    </div>
  {:else if rsvpStage === 2}
    <div class="attendance-wrapper">
      <span class="attendance-desc">Wie kom almal saam?</span>
      {#each guestData as guest}
        <div class="guest-wrapper">
          <span class="guest-name">{guest.fullname}</span>
          <div class="split-button">
            <button class:selected={guest.attendance === 1} on:click={() => handleGuestAttendance(guest.id, 1)}
              >Ja</button
            >
            <button class:selected={guest.attendance === 0} on:click={() => handleGuestAttendance(guest.id, 0)}
              >Nee</button
            >
          </div>
        </div>
        {#if guest.plusone}
          <span class="attendance-desc">Indien jy 'n +1 saambring, gee hulle naam deur.</span>
          <input class="fn-input" placeholder="Volle Naam en Van" bind:value={guest.plusoneName} />
        {/if}
      {/each}
      <button class="find-invite-btn" on:click={increaseRsvpStage}>Volgende</button>
      <button class="find-invite-btn" on:click={decreaseRsvpStage}>Terug</button>
    </div>
  {:else if rsvpStage === 3}
    <div class="accommodation-wrapper">
      <span class="attendance-desc">Kies jou verblyf opsies</span>
      {#each guestData as guest}
        {#if guest.attendance === 1}
        <div class="guest-wrapper">
          <span class="guest-name">{guest.fullname}</span>
          <div class="acc-list">
            <select
              class="acc-select"
              bind:value={guest.accommodation}
              on:change={(event) => handleGuestAccomodation(guest.id, event)}
              >
              {#each options as option}
              <option class="acc-option" value={option.value}><span class="test">{option.text}</span></option>
              {/each}
            </select>
          </div>
        </div>
        {/if}
      {/each}
      <button class="find-invite-btn" on:click={increaseRsvpStage}>Volgende</button>
      <button class="find-invite-btn" on:click={decreaseRsvpStage}>Terug</button>
    </div>
  {:else if rsvpStage === 4}
    <div class="email-wrapper">
      <span class="email-desc"
        >Epos addres - baie belangrik sodat Louvain die faktuur vir die verblyf na jou kan stuur</span
      >
      {#if !emailValid}
       <br /><br /><span class="email-desc">Maak asb seker dat dit 'n geldige epos is!</span> 
      {/if}
      <input class="email-input" type="email" placeholder="Epos Addres" bind:value={email} on:change={handleEmailChange} required/>
      <button class="find-invite-btn" on:click={saveGuestResponse} disabled={!emailValid}>Volgende</button>
      <button class="find-invite-btn" on:click={decreaseRsvpStage}>Terug</button>
    </div>
  {:else if rsvpStage === 5}
    <div class="rsvp-done">
      <span class="rsvp-d-desc">Ons sien uit om ons spesiale dag met julle te deel! <br /><br />
        Daar sal 'n epos gestuur word om die RSVP te bevestig.
      </span>
    </div>
  {:else if rsvpStage === -1}
  <div class="rsvp-done">
    <span class="rsvp-d-desc">Dankie dat jy laat weet het dat julle nie die dag kan bywoon nie.<br /><br />
      Indien jy dit in die toekoms kan maak, kan jy altyd weer hierdie proses volg om te RSVP!
    </span>
  </div>
  {/if}

</div>

<style>
  .email-input {
    margin: 15px 0px 15px 0px;
    width: 450px;
    box-sizing: border-box;
    max-width: 100%;
    border: 1px solid #ad925d;
    color: #111;
    background-color: azure;
    font-family: "QueenSides";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
    max-width: 100%;
  }

  .fn-input:focus {
    outline: 1px solid #ad925d;
    color: #111;
  }

  .acc-select {
    padding: 10px;
    font-family: "QueenSides";
    font-size: 20px;
    border: 1px solid #ad925d;
    box-sizing: border-box;
    box-shadow: none;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  .acc-select:focus {
    outline: 1px solid #ad925d;
    color: #111;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  .acc-list {
    width: 100%;
  }

  @media (max-width: 500px) {
    .acc-select {
      margin-top: 5px;
      margin-bottom: 20px;
      width: 100%;
      box-sizing: border-box;
    }

    .guest-wrapper {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      user-select: none;
    }

    .split-button {
      margin-top: 5px;
      margin-bottom: 20px;
    }
  }

  .guest-name {
    font-family: "QueenSides";
    color: #111;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    font-size: 20px;
    margin-top: 5px;
    margin-bottom: 20px;
    user-select: none;
  }

  @media (min-width: 501px) {
    .guest-wrapper {
      margin: 15px 0px 15px 0px;
      width: 450px;
      box-sizing: border-box;
      max-width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }

    .acc-select {
      width: 200px;
    }
  }

  .split-button {
    display: flex;
    width: 200px;
    border: 1px solid #ad925d;
    border-radius: 2px;
    overflow: hidden;
  }

  .split-button button {
    flex: 1;
    padding: 10px;
    background-color: azure;
    color: #ad925d;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .split-button button:first-child {
    border-right: 1px solid #ad925d; /* Creates the split effect */
  }

  .split-button button:hover {
    background-color: rgba(173, 146, 93, 0.3);
  }

  .split-button button:active {
    background-color: rgba(173, 146, 93, 0.3);
  }

  .selected {
    background-color: rgba(173, 146, 93, 0.3) !important;
  }

  .found-inv-wrapper,
  .attendance-wrapper,
  .email-wrapper,
  .accommodation-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    user-select: none;
  }

  .form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .fn-input,
  .find-invite-btn {
    margin: 15px 0px 15px 0px;
    width: 450px;
    box-sizing: border-box;
    max-width: 100%;
  }

  .fn-input {
    border: 1px solid #ad925d;
    color: #111;
    background-color: azure;
    font-family: "QueenSides";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
    max-width: 100%;
  }

  .fn-input:focus {
    outline: 1px solid #ad925d;
    color: #111;
  }

  .find-invite-btn {
    border: 1px solid #ad925d;
    color: #ad925d;
    background-color: azure;
    cursor: pointer;
    font-family: "QueenSides";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
    max-width: 100%;
  }

  .find-invite-btn:hover {
    background-color: azure;
    color: #ad925d;
  }

  .rsvp-desc,
  .attendance-desc,
  .email-desc,
  .rsvp-d-desc {
    font-family: "QueenSides";
    color: #ad925d;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    font-size: 20px;
    user-select: none;
  }

  .general-text {
    font-family: "QueenSides";
    color: #ad925d;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    font-size: 20px;
    user-select: none;
  }

  @media (min-width: 1000px) {
    .rsvp-desc,
    .attendance-desc,
    .email-desc,
    .rsvp-d-desc {
      font-size: 24px;
    }
  }
</style>
