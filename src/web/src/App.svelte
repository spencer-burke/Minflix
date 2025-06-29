<script>
/*
loggedIn:
- this controls the visibility of the login and register buttons
- this also controls whether the user is logged in or not
- we still need the navbar element
*/
	import Navbar from './lib/Navbar.svelte';
	let loggedIn = $state(false);
</script>

<main>
	<Navbar loggedIn={loggedIn} />
	<button onclick={() => loggedIn = !loggedIn}>
		from the app.svelte file
		{loggedIn ? 'Logout' : 'Login'}
	</button>
</main> 