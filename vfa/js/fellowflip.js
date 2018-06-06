;(function(e,t,n){function i(n,s){if(!t[n]){if(!e[n]){var o=typeof require=="function"&&require;if(!s&&o)return o(n,!0);if(r)return r(n,!0);throw new Error("Cannot find module '"+n+"'")}var u=t[n]={exports:{}};e[n][0].call(u.exports,function(t){var r=e[n][1][t];return i(r?r:t)},u,u.exports)}return t[n].exports}var r=typeof require=="function"&&require;for(var s=0;s<n.length;s++)i(n[s]);return i})({1:[function(require,module,exports){
// index.js

var flip = flippant.flip
var event = require('./event')

document.addEventListener('click', function(e) {
  if (e.target.classList.contains('btnflip')) {
    e.preventDefault()
    var flipper = e.target.parentNode.parentNode
    var back
    var name = '<h2 style="color: white">' + flipper.querySelector('h3').innerText + '</h2>'
    var scyr = '<h3 style="color: white">' + flipper.querySelector('p').innerText + '</h3>'
    var button = '<br><button class="btn">Back</button>'


    if (e.target.classList.contains('fellow1')) {
      back = flip(flipper, name + scyr + "Ada is currently working on a master’s in Engineering Management at Johns Hopkins. She has been part of several design teams working on everything from prosthetic devices to embedded electronics. Her interest in entrepreneurship was sparked while exploring the business side of product development as an intern in Hopkins Tech Transfer. Outside of the lab, she likes volleyball and yoga and looks forward to reading the end of A Song of Ice and Fire"  + button, 'modal')
      }

    if (e.target.classList.contains('fellow2')) {
      back = flip(flipper, name + scyr + "Aldo graduated from Columbia University with a degree in mechanical engineering. With a passion for design and innovation, Aldo has developed a drone system for the National Geospatial Intelligence Agency in addition to a high precision delta robot. Interning as a consult at both Accenture and Booz Allen, Aldo has learned business development when it comes to emerging technology. When not sketching up a new idea, you can find Aldo enjoying great conversation over food." + button, 'modal')
    }
    
    if (e.target.classList.contains('fellow3')) {
      back = flip(flipper, name + scyr + "Alex is studying Marketing and Finance at Boston University&#8217;s School of Management with a minor in Psychology. After having internships at corporations like Micron Technology and Under Armour, he hopes that a startup culture an provide the fast-paced, fulfilling, and fun work environment that he desires. Working at Crimson Hexagon, a social media analytics startup in Boston provided exactly that, where he transformed social data into engaging content on the company blog. At Boston University, he has held many leadership roles within the business fraternity, Alpha Kappa Psi, as well as serving as a Career Peer mentor for younger students. His interests include the poetics of rap music, online education platforms, and playing pick-up basketball." + button, 'modal')
    }

    if (e.target.classList.contains('fellow4')) {
      back = flip(flipper, name + scyr + "Alexa graduated from Macalester College in St. Paul, MN, with a dual degree in International Studies and Geography. Passionate about social ventures and poverty alleviation, Alexa interned at USAID as a Congressional and Events/Protocol Intern in Washington D.C., worked for the startup FINNEGANS, a social venture which produces high quality beer, as an entrepreneurship/GIS intern in Minneapolis, won a grant of $7,500 for the international non-profit Rising Minds and then served as the Summer Regional Director for the organization in Guatemala. Recently, she completed a fellowship with Accion International, working with a for-profit bank in Guatemala. In her free time, Alexa enjoys rock climbing, boxing, playing soccer, learning Mayan languages, and exploring new cities. " + button, 'modal')
    }

    if (e.target.classList.contains('fellow5')) {
      var cheese = 'Alex (@Toivikki) will graduate from Washington &#038; Lee University with a major in Computer Science and concentrations in Chemistry, Engineering, and Business. At W&#038;L, he founded and led both the Club Swimming Team and a chapter of the Association for Computing Machinery. Alex also founded SOS4Cancer, a DC based non profit organization determined to improve the lives of teens and children fighting cancer through the efforts of their peers. For the past two summers, he has explored different fields in computer science ranging from emotion recognition to distributed cyber security. His passion for entrepreneurship allowed him to participate in the 2014 National Student Advertising Competition. Most recently, Alex consulted on the development of new markets for SourceFuse, a digital product development​ startup based in Florida. Alex ​is an accomplished violist, violinist, and singer; an avid outdoorsman and swimmer; and a formidable board game opponent.'
      back = flip(flipper, name + scyr + cheese + button, 'modal')
    }

    if (e.target.classList.contains('fellow6')) {
      back = flip(flipper, name + scyr + "Andrew graduated from Johns Hopkins University where he earned a Master&#8217;s in Music and also pursued doctoral coursework. Prior to coming to JHU, Andrew completed undergraduate degrees in both French and Music from Oberlin College where he was a recipient of the Conservatory Deans Talent Grant, outreach member for LOCHOS linguistic outreach, and principal flutist of the Oberlin Orchestra. Andrew completed studies abroad in Paris at La Sorbonne, Nice, and Quebec." + button, 'modal')
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