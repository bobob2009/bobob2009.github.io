;(function(e,t,n){function i(n,s){if(!t[n]){if(!e[n]){var o=typeof require=="function"&&require;if(!s&&o)return o(n,!0);if(r)return r(n,!0);throw new Error("Cannot find module '"+n+"'")}var u=t[n]={exports:{}};e[n][0].call(u.exports,function(t){var r=e[n][1][t];return i(r?r:t)},u,u.exports)}return t[n].exports}var r=typeof require=="function"&&require;for(var s=0;s<n.length;s++)i(n[s]);return i})({1:[function(require,module,exports){
// index.js

var flip = flippant.flip
var event = require('./event')

document.addEventListener('click', function(e) {
  if (e.target.classList.contains('btnflip')) {
    e.preventDefault()
    var flipper = e.target.parentNode.parentNode
    var back
    var rowst = '<span class=row>'
    var colst = '<span style="width:50%">'
    var name = '<h2 style="color: white">' + flipper.querySelector('h3').innerText + '</h2>'
    var coyr = '<h3 style="color: white">' + flipper.querySelector('p').innerText + '</h3>'
    var button = '<br><button class="btn">Back</button>'
    var colen = '</span>'
    var rowen = '</span>'
    var img1 = '<img alt="" src="images/homepage/Background%20Kate%20Leisy.jpg" />'
    var img2 = '<img alt="" src="images/homepage/RebirthRealty.jpg" />'
    var img3 = '<img alt="" src="images/homepage/TernPro.png" />'
    var img4 = '<img alt="" src="images/homepage/hetali2.jpg" />'
    var img5 = '<img alt="" src="images/homepage/Picture3.png" />'


    if (e.target.classList.contains('fellow1')) {
      back = flip(flipper, rowst + colst + name + coyr + "Kate has had an explosive start as a Venture for America fellow. While working on the Curalate team, she teamed up with another 2013er, Zubin Teherani, to raise $18,000 towards the creation of Bandaloo. Bandaloo is a weekend long event that connects local musicians, supports them with coaching from experienced artists and music industry leaders, and provides them with a spotlight to perform. Read about Kate and Bandaloo in the <u><a href='http://www.huffingtonpost.com/kate-leisy/putting-the-us-back-in-music_b_4418919.html' target='_blank'>Huffington Post</a></u> and check out her crowdfunding page on <u><a href='http://www.rockethub.com/projects/36000-bandaloo-connecting-local-musicians-and-creating-unique-music' target='_blank'>Rocket Hub.</a></u>" + button + colen + colst + img1 + colen + rowen, 'modal')
    }
    
    if (e.target.classList.contains('fellow2')) {
      back = flip(flipper, rowst + colst + name + coyr + "Scott has been a major source of inspiration for VFA and the Detroit Community. Scott and his team of 2012 fellows Max Nussenbaum, Tim Dingham, and Sean Jackson, have started Rebirth Realty in their quest to transform an abandoned Detroit house into an amazing living space for future generations of VFA Fellows. Through VFA’s Innovation Fund Challenge, and other prizes, Rebirth has raised over $16,000 towards purchasing and renovating a foreclosed house. Addtionally, Scott, Max, and Tim are in the midst of launching Castle, a new application that allows for better communication between landlords and tenants. <u><a href=’http://rebirthrealtydetroit.com/’ target=’_blank’>Follow the Rebirth project</a></u> and be sure to check out <u><a href=’http://blog.entercastle.com/’ target=’_blank’>Castle’s blog.</a></u></p>" + button + colen + colst + img2 + colen + rowen, 'modal')
    }
    
    if (e.target.classList.contains('fellow3')) {
      back = flip(flipper, rowst + colst + name + coyr + "Brian has made a significant impact in the business world since he started with VFA. After excelling at Bizdom in Detroit, he worked with other fellows to found Startup Effect and TernPro. The <u><a href=’http://www.startupeffect.org/learn/’ target=’_blank’>Startup Effect</a></u> is an enrichment program for middle school students in transitioning U.S. cities to gain confidence and skills through action-oriented, entrepreneurial activities and challenges. <u><a href=’http://ternpro.com/pages/how-it-works’ target=’_blank’>TernPro</a></u> was created to show the amazing stories of people and organizations in an immersive, engaging way. " + button + colen + colst + img3 + colen + rowen, 'modal')
    }
    
    if (e.target.classList.contains('fellow4')) {
      back = flip(flipper, rowst + colst + name + coyr + "Hetali is a Public Policy and Chemistry major at UNC, and wants to spend the rest of her life helping people understand why science matters to them. All credit for her interest in entrepreneurship and strong attraction to VFA’s mission-driven model goes to four years in Nourish-UNC, a student group that allowed her to start a business and understand the power inherent in communities. She spent summers teaching 9th grade science in Philly with Breakthrough Collaborative, working at USAID through the Washington Leadership Program, and reporting for STEMwire at Reese News Lab. Hetali loves sci-fi/fantasy literature, sunshine and eating local, and live-tweets whenever the occasion calls for it. Follow her on Twitter <u><a href=’http://twitter.com/HetaliLodaya’ target=’_blank’>@HetaliLodaya</a></u>." + button + colen + colst + img4 + colen + rowen, 'modal')
    }
    
    if (e.target.classList.contains('fellow5')) {
      back = flip(flipper, rowst + colst + name + coyr + "Andrew Yang is the dynamic founder of Venture for America.  Early this year, he published a book called 'Smart People Should Build Things.' His vision and dedication have helped create the Notorious VFA brand." + button + colen + colst + img5 + colen + rowen, 'modal')
    }

    back.addEventListener('click', function(e) {
      if (e.target.classList.contains('btn')) {
        event.trigger(back, 'close')
      }
    })

  }
})


},{"./event":2}],2:[function(require,module,exports){
exports.trigger = function(elm, event_name, data) {
  var evt = new CustomEvent(event_name, data)
  elm.dispatchEvent(evt)
}
},{}]},{},[1])
;